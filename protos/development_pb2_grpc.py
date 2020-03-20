# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protos import data_pb2 as protos_dot_data__pb2
from protos import development_pb2 as protos_dot_development__pb2


class EditorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.New = channel.unary_stream(
        '/Editor/New',
        request_serializer=protos_dot_development__pb2.NewStrategyRequest.SerializeToString,
        response_deserializer=protos_dot_data__pb2.Chunk.FromString,
        )
    self.Save = channel.stream_unary(
        '/Editor/Save',
        request_serializer=protos_dot_data__pb2.Chunk.SerializeToString,
        response_deserializer=protos_dot_development__pb2.SaveResponse.FromString,
        )
    self.Push = channel.stream_unary(
        '/Editor/Push',
        request_serializer=protos_dot_data__pb2.Chunk.SerializeToString,
        response_deserializer=protos_dot_development__pb2.PushResponse.FromString,
        )
    self.GetStrategy = channel.unary_stream(
        '/Editor/GetStrategy',
        request_serializer=protos_dot_development__pb2.StrategyRequest.SerializeToString,
        response_deserializer=protos_dot_data__pb2.Chunk.FromString,
        )


class EditorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def New(self, request, context):
    """for developing and editing strategies
    rpc BackTest (BackTestRequest) returns (stream PerformancePacket);
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Save(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Push(self, request_iterator, context):
    """pushes the directory into the server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStrategy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EditorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'New': grpc.unary_stream_rpc_method_handler(
          servicer.New,
          request_deserializer=protos_dot_development__pb2.NewStrategyRequest.FromString,
          response_serializer=protos_dot_data__pb2.Chunk.SerializeToString,
      ),
      'Save': grpc.stream_unary_rpc_method_handler(
          servicer.Save,
          request_deserializer=protos_dot_data__pb2.Chunk.FromString,
          response_serializer=protos_dot_development__pb2.SaveResponse.SerializeToString,
      ),
      'Push': grpc.stream_unary_rpc_method_handler(
          servicer.Push,
          request_deserializer=protos_dot_data__pb2.Chunk.FromString,
          response_serializer=protos_dot_development__pb2.PushResponse.SerializeToString,
      ),
      'GetStrategy': grpc.unary_stream_rpc_method_handler(
          servicer.GetStrategy,
          request_deserializer=protos_dot_development__pb2.StrategyRequest.FromString,
          response_serializer=protos_dot_data__pb2.Chunk.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Editor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class EnvironmentStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Setup = channel.unary_unary(
        '/Environment/Setup',
        request_serializer=protos_dot_development__pb2.SetupRequest.SerializeToString,
        response_deserializer=protos_dot_development__pb2.SetupResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/Environment/Delete',
        request_serializer=protos_dot_development__pb2.DeleteRequest.SerializeToString,
        response_deserializer=protos_dot_development__pb2.DeleteResponse.FromString,
        )


class EnvironmentServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Setup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EnvironmentServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Setup': grpc.unary_unary_rpc_method_handler(
          servicer.Setup,
          request_deserializer=protos_dot_development__pb2.SetupRequest.FromString,
          response_serializer=protos_dot_development__pb2.SetupResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=protos_dot_development__pb2.DeleteRequest.FromString,
          response_serializer=protos_dot_development__pb2.DeleteResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Environment', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
