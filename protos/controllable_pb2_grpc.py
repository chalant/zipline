# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos import clock_pb2 as protos_dot_clock__pb2
from protos import controller_pb2 as protos_dot_controller__pb2
from protos import data_pb2 as protos_dot_data__pb2


class ControllableStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UpdateParameters = channel.unary_unary(
        '/Controllable/UpdateParameters',
        request_serializer=protos_dot_controller__pb2.ParametersUpdateRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Initialize = channel.stream_unary(
        '/Controllable/Initialize',
        request_serializer=protos_dot_data__pb2.Chunk.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ClockUpdate = channel.unary_unary(
        '/Controllable/ClockUpdate',
        request_serializer=protos_dot_clock__pb2.ClockEvent.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UpdateAccount = channel.stream_unary(
        '/Controllable/UpdateAccount',
        request_serializer=protos_dot_data__pb2.Chunk.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Stop = channel.unary_unary(
        '/Controllable/Stop',
        request_serializer=protos_dot_controller__pb2.StopRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Watch = channel.unary_unary(
        '/Controllable/Watch',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.StopWatching = channel.unary_unary(
        '/Controllable/StopWatching',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ControllableServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UpdateParameters(self, request, context):
    """A service that is called by a controller
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Initialize(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClockUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateAccount(self, request_iterator, context):
    """for updating positions, transactions etc.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Watch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopWatching(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllableServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UpdateParameters': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateParameters,
          request_deserializer=protos_dot_controller__pb2.ParametersUpdateRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Initialize': grpc.stream_unary_rpc_method_handler(
          servicer.Initialize,
          request_deserializer=protos_dot_data__pb2.Chunk.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ClockUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.ClockUpdate,
          request_deserializer=protos_dot_clock__pb2.ClockEvent.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UpdateAccount': grpc.stream_unary_rpc_method_handler(
          servicer.UpdateAccount,
          request_deserializer=protos_dot_data__pb2.Chunk.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=protos_dot_controller__pb2.StopRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Watch': grpc.unary_unary_rpc_method_handler(
          servicer.Watch,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'StopWatching': grpc.unary_unary_rpc_method_handler(
          servicer.StopWatching,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Controllable', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
