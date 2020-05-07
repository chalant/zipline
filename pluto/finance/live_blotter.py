from zipline.finance.blotter import blotter

from pluto.finance import order as odr
from pluto.coms.utils import conversions

from protos import broker_pb2


class LiveBlotter(blotter.Blotter):
    def __init__(self, broker, cancel_policy=None):
        '''

        Parameters
        ----------
        broker: pluto.broker.broker_stub.BrokerStub
        cancel_policy
        '''
        super(LiveBlotter, self).__init__(cancel_policy)

        self._broker = broker
        self._orders = {}
        self._new_orders = {}

        self._transactions = []
        self._closed_orders = []
        self._commissions = []

        self._orders_placed = False

    @property
    def new_orders(self):
        #return a tuple so that values can't be changed
        return tuple(self._new_orders.values())

    @new_orders.setter
    def new_orders(self, value):
        #resets the new orders
        if not self._orders_placed:
            #send orders buffered orders to the broker once before resetting
            def generator(orders):
                for order in orders:
                    yield conversions.to_proto_order(order)

            # send orders to broker before resetting
            orders = self._orders
            for order in self._broker.PlaceOrders(generator(
                    self._new_orders.values())):
                order = conversions.to_zp_order(order)
                orders[order.id] = order
            self._orders_placed = True
        self._new_orders = {}

    def get_transactions(self, bar_data):
        return self._transactions, self._commissions, self._closed_orders

    def orders(self):
        return self._orders

    def order(self, asset, amount, style, order_id=None):
        if amount == 0:
            # Don't bother placing orders for 0 shares.
            return None

        elif amount > self.max_shares:
            # Arbitrary limit of 100 billion (US) shares will never be
            # exceeded except by a buggy algorithm.
            raise OverflowError("Can't order more than %d shares" %
                                self.max_shares)

        is_buy = (amount > 0)
        order = odr.Order(
            dt=self.current_dt,
            asset=asset,
            amount=amount,
            stop=style.get_stop_price(is_buy),
            limit=style.get_limit_price(is_buy)
        )
        id_ = order.id
        self._new_orders[id_] = order
        # mark so that the new orders can be sent to the broker
        self._orders_placed = False
        return id_

    def hold(self, order_id, reason=''):
        pass

    def reject(self, order_id, reason=''):
        pass

    def cancel(self, order_id, relay_status=True):
        try:
            # attempt to cancel new orders that have not been placed yet
            self._new_orders.pop(order_id)
        except KeyError:
            # send cancel request to broker
            self._broker.CancelOrder(
                broker_pb2.CancelRequest(order_id=order_id))

    def cancel_all_orders_for_asset(self, asset, warn=False, relay_status=True):
        self._broker.CancelAllOrdersForAsset(
            conversions.to_proto_asset(asset))

    def execute_cancel_policy(self, event):
        self._broker.ExecuteCancelPolicy(
            broker_pb2.Event(event_type=event))

    def process_splits(self, splits):
        pass

    def update(self, dt, broker_data):
        # called each minute
        commissions = self._commissions
        closed_orders = self._closed_orders
        transactions = self._transactions

        orders = self._orders
        for transaction in broker_data.transactions:
            order_id = transaction.order_id
            o = orders.get(order_id, None)
            if o:
                transactions.append(transaction)

        for commission in broker_data.commissions:
            order = commission.order
            order_id = order.order_id
            o = orders.get(order_id, None)
            if o:
                commissions.append({
                    'asset': commission.asset,
                    'cost': commission.cost,
                    'order': order
                })

            orders[order_id] = order  # update the order state
            if not order.open:
                closed_orders.append(order)

    def prune_orders(self, closed_orders):
        orders = self._orders
        for order in closed_orders:
            try:
                del orders[order.order_id]
            except KeyError:
                pass

        self._transactions.clear()
        self._commissions.clear()
        self._closed_orders.clear()
