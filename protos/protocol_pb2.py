# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/protocol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protos import assets_pb2 as protos_dot_assets__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/protocol.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15protos/protocol.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x13protos/assets.proto\"\x8b\x03\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\t\x12&\n\x02\x64t\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12+\n\x07\x63reated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\x05\x61sset\x18\x05 \x01(\x0b\x32\x06.Asset\x12\x0e\n\x06\x61mount\x18\x06 \x01(\x02\x12\x0e\n\x06\x66illed\x18\x07 \x01(\x05\x12\x12\n\ncommission\x18\x08 \x01(\x02\x12\x1d\n\x06status\x18\x0e \x01(\x0e\x32\r.Order.Status\x12\x0c\n\x04stop\x18\t \x01(\x02\x12\r\n\x05limit\x18\n \x01(\x02\x12\x14\n\x0cstop_reached\x18\x0b \x01(\x08\x12\x15\n\rlimit_reached\x18\x0c \x01(\x08\x12\x17\n\x0f\x62roker_order_id\x18\r \x01(\x03\"D\n\x06Status\x12\x08\n\x04OPEN\x10\x00\x12\n\n\x06\x46ILLED\x10\x01\x12\x0c\n\x08\x43\x41NCELED\x10\x02\x12\x0c\n\x08REJECTED\x10\x03\x12\x08\n\x04HELD\x10\x04\"\x92\x01\n\x08Position\x12\x15\n\x05\x61sset\x18\x01 \x01(\x0b\x32\x06.Asset\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x12\n\ncost_basis\x18\x03 \x01(\x02\x12\x17\n\x0flast_sale_price\x18\x04 \x01(\x02\x12\x32\n\x0elast_sale_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd0\x03\n\x07\x41\x63\x63ount\x12\x14\n\x0csettled_cash\x18\x01 \x01(\x02\x12\x18\n\x10\x61\x63\x63rued_interest\x18\x02 \x01(\x02\x12\x14\n\x0c\x62uying_power\x18\x03 \x01(\x02\x12\x18\n\x10\x65quity_with_loan\x18\x04 \x01(\x02\x12\x1d\n\x15total_positions_value\x18\x05 \x01(\x02\x12 \n\x18total_positions_exposure\x18\x06 \x01(\x02\x12\x13\n\x0bregt_equity\x18\x07 \x01(\x02\x12\x13\n\x0bregt_margin\x18\x08 \x01(\x02\x12\"\n\x1ainitial_margin_requirement\x18\t \x01(\x02\x12&\n\x1emaintenance_margin_requirement\x18\n \x01(\x02\x12\x17\n\x0f\x61vailable_funds\x18\x0b \x01(\x02\x12\x18\n\x10\x65xcess_liquidity\x18\x0c \x01(\x02\x12\x0f\n\x07\x63ushion\x18\r \x01(\x02\x12\x1c\n\x14\x64\x61y_trades_remaining\x18\x0e \x01(\x02\x12\x10\n\x08leverage\x18\x0f \x01(\x02\x12\x14\n\x0cnet_leverage\x18\x10 \x01(\x02\x12\x17\n\x0fnet_liquidation\x18\x11 \x01(\x02\x12\x0b\n\x03sma\x18\x12 \x01(\x02\"\x86\x02\n\tPortfolio\x12\x11\n\tcash_flow\x18\x01 \x01(\x02\x12\x15\n\rstarting_cash\x18\x02 \x01(\x02\x12\x17\n\x0fportfolio_value\x18\x03 \x01(\x02\x12\x0b\n\x03pnl\x18\x04 \x01(\x02\x12\x0f\n\x07returns\x18\x05 \x01(\x02\x12\x0c\n\x04\x63\x61sh\x18\x06 \x01(\x02\x12%\n\tpositions\x18\x07 \x03(\x0b\x32\x12.AssetPositionPair\x12.\n\nstart_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0fpositions_value\x18\t \x01(\x02\x12\x1a\n\x12positions_exposure\x18\n \x01(\x02\"E\n\x11\x41ssetPositionPair\x12\x13\n\x03key\x18\x01 \x01(\x0b\x32\x06.Asset\x12\x1b\n\x08position\x18\x02 \x01(\x0b\x32\t.Positionb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,protos_dot_assets__pb2.DESCRIPTOR,])



_ORDER_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Order.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILLED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HELD', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=407,
  serialized_end=475,
)
_sym_db.RegisterEnumDescriptor(_ORDER_STATUS)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Order.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dt', full_name='Order.dt', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='Order.reason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='Order.created', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset', full_name='Order.asset', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Order.amount', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filled', full_name='Order.filled', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commission', full_name='Order.commission', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='Order.status', index=8,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='Order.stop', index=9,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='Order.limit', index=10,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_reached', full_name='Order.stop_reached', index=11,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit_reached', full_name='Order.limit_reached', index=12,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='broker_order_id', full_name='Order.broker_order_id', index=13,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ORDER_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=475,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset', full_name='Position.asset', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Position.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost_basis', full_name='Position.cost_basis', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_sale_price', full_name='Position.last_sale_price', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_sale_date', full_name='Position.last_sale_date', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=478,
  serialized_end=624,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='settled_cash', full_name='Account.settled_cash', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accrued_interest', full_name='Account.accrued_interest', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buying_power', full_name='Account.buying_power', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='equity_with_loan', full_name='Account.equity_with_loan', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_positions_value', full_name='Account.total_positions_value', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_positions_exposure', full_name='Account.total_positions_exposure', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regt_equity', full_name='Account.regt_equity', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regt_margin', full_name='Account.regt_margin', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_margin_requirement', full_name='Account.initial_margin_requirement', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maintenance_margin_requirement', full_name='Account.maintenance_margin_requirement', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_funds', full_name='Account.available_funds', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='excess_liquidity', full_name='Account.excess_liquidity', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cushion', full_name='Account.cushion', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_trades_remaining', full_name='Account.day_trades_remaining', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leverage', full_name='Account.leverage', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='net_leverage', full_name='Account.net_leverage', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='net_liquidation', full_name='Account.net_liquidation', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sma', full_name='Account.sma', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=627,
  serialized_end=1091,
)


_PORTFOLIO = _descriptor.Descriptor(
  name='Portfolio',
  full_name='Portfolio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cash_flow', full_name='Portfolio.cash_flow', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starting_cash', full_name='Portfolio.starting_cash', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portfolio_value', full_name='Portfolio.portfolio_value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pnl', full_name='Portfolio.pnl', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='returns', full_name='Portfolio.returns', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cash', full_name='Portfolio.cash', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positions', full_name='Portfolio.positions', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='Portfolio.start_date', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positions_value', full_name='Portfolio.positions_value', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positions_exposure', full_name='Portfolio.positions_exposure', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1094,
  serialized_end=1356,
)


_ASSETPOSITIONPAIR = _descriptor.Descriptor(
  name='AssetPositionPair',
  full_name='AssetPositionPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='AssetPositionPair.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='AssetPositionPair.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1358,
  serialized_end=1427,
)

_ORDER.fields_by_name['dt'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ORDER.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ORDER.fields_by_name['asset'].message_type = protos_dot_assets__pb2._ASSET
_ORDER.fields_by_name['status'].enum_type = _ORDER_STATUS
_ORDER_STATUS.containing_type = _ORDER
_POSITION.fields_by_name['asset'].message_type = protos_dot_assets__pb2._ASSET
_POSITION.fields_by_name['last_sale_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PORTFOLIO.fields_by_name['positions'].message_type = _ASSETPOSITIONPAIR
_PORTFOLIO.fields_by_name['start_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASSETPOSITIONPAIR.fields_by_name['key'].message_type = protos_dot_assets__pb2._ASSET
_ASSETPOSITIONPAIR.fields_by_name['position'].message_type = _POSITION
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['Portfolio'] = _PORTFOLIO
DESCRIPTOR.message_types_by_name['AssetPositionPair'] = _ASSETPOSITIONPAIR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), dict(
  DESCRIPTOR = _ORDER,
  __module__ = 'protos.protocol_pb2'
  # @@protoc_insertion_point(class_scope:Order)
  ))
_sym_db.RegisterMessage(Order)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'protos.protocol_pb2'
  # @@protoc_insertion_point(class_scope:Position)
  ))
_sym_db.RegisterMessage(Position)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT,
  __module__ = 'protos.protocol_pb2'
  # @@protoc_insertion_point(class_scope:Account)
  ))
_sym_db.RegisterMessage(Account)

Portfolio = _reflection.GeneratedProtocolMessageType('Portfolio', (_message.Message,), dict(
  DESCRIPTOR = _PORTFOLIO,
  __module__ = 'protos.protocol_pb2'
  # @@protoc_insertion_point(class_scope:Portfolio)
  ))
_sym_db.RegisterMessage(Portfolio)

AssetPositionPair = _reflection.GeneratedProtocolMessageType('AssetPositionPair', (_message.Message,), dict(
  DESCRIPTOR = _ASSETPOSITIONPAIR,
  __module__ = 'protos.protocol_pb2'
  # @@protoc_insertion_point(class_scope:AssetPositionPair)
  ))
_sym_db.RegisterMessage(AssetPositionPair)


# @@protoc_insertion_point(module_scope)
