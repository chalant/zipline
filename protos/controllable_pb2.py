# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/controllable.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos import data_bundle_pb2 as protos_dot_data__bundle__pb2
from protos import broker_pb2 as protos_dot_broker__pb2
from protos import controller_pb2 as protos_dot_controller__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protos import clock_pb2 as protos_dot_clock__pb2
from protos import data_pb2 as protos_dot_data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/controllable.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19protos/controllable.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x18protos/data_bundle.proto\x1a\x13protos/broker.proto\x1a\x17protos/controller.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x12protos/clock.proto\x1a\x11protos/data.proto\"Y\n\nInitParams\x12\"\n\x06\x64omain\x18\x01 \x01(\x0b\x32\x12.CompoundDomainDef\x12\x10\n\x08strategy\x18\x02 \x01(\x0c\x12\x15\n\rcapital_ratio\x18\x03 \x01(\x02\"y\n\rUpdateRequest\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\x05\x65vent\x18\x02 \x01(\x0e\x32\x06.Event\x12\"\n\x0c\x62roker_state\x18\x03 \x01(\x0b\x32\x0c.BrokerState\"\r\n\x0bUpdateReply2\xef\x02\n\x0c\x43ontrollable\x12\x33\n\x10UpdateDataBundle\x12\x05.Data\x1a\x16.google.protobuf.Empty(\x01\x12\x44\n\x10UpdateParameters\x12\x18.ParametersUpdateRequest\x1a\x16.google.protobuf.Empty\x12-\n\nInitialize\x12\x05.Data\x1a\x16.google.protobuf.Empty(\x01\x12\x32\n\x0b\x43lockUpdate\x12\x0b.ClockEvent\x1a\x16.google.protobuf.Empty\x12\x30\n\rUpdateAccount\x12\x05.Data\x1a\x16.google.protobuf.Empty(\x01\x12\x31\n\x0eUpdateCalendar\x12\x05.Data\x1a\x16.google.protobuf.Empty(\x01\x12\x1c\n\x04Stop\x12\x0b.StopParams\x1a\x05.Data0\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,protos_dot_data__bundle__pb2.DESCRIPTOR,protos_dot_broker__pb2.DESCRIPTOR,protos_dot_controller__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,protos_dot_clock__pb2.DESCRIPTOR,protos_dot_data__pb2.DESCRIPTOR,])




_INITPARAMS = _descriptor.Descriptor(
  name='InitParams',
  full_name='InitParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='InitParams.domain', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='InitParams.strategy', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capital_ratio', full_name='InitParams.capital_ratio', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=202,
  serialized_end=291,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='UpdateRequest.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='UpdateRequest.event', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='broker_state', full_name='UpdateRequest.broker_state', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=293,
  serialized_end=414,
)


_UPDATEREPLY = _descriptor.Descriptor(
  name='UpdateReply',
  full_name='UpdateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=416,
  serialized_end=429,
)

_INITPARAMS.fields_by_name['domain'].message_type = protos_dot_data__bundle__pb2._COMPOUNDDOMAINDEF
_UPDATEREQUEST.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPDATEREQUEST.fields_by_name['event'].enum_type = protos_dot_clock__pb2._EVENT
_UPDATEREQUEST.fields_by_name['broker_state'].message_type = protos_dot_broker__pb2._BROKERSTATE
DESCRIPTOR.message_types_by_name['InitParams'] = _INITPARAMS
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateReply'] = _UPDATEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitParams = _reflection.GeneratedProtocolMessageType('InitParams', (_message.Message,), dict(
  DESCRIPTOR = _INITPARAMS,
  __module__ = 'protos.controllable_pb2'
  # @@protoc_insertion_point(class_scope:InitParams)
  ))
_sym_db.RegisterMessage(InitParams)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREQUEST,
  __module__ = 'protos.controllable_pb2'
  # @@protoc_insertion_point(class_scope:UpdateRequest)
  ))
_sym_db.RegisterMessage(UpdateRequest)

UpdateReply = _reflection.GeneratedProtocolMessageType('UpdateReply', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREPLY,
  __module__ = 'protos.controllable_pb2'
  # @@protoc_insertion_point(class_scope:UpdateReply)
  ))
_sym_db.RegisterMessage(UpdateReply)



_CONTROLLABLE = _descriptor.ServiceDescriptor(
  name='Controllable',
  full_name='Controllable',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=432,
  serialized_end=799,
  methods=[
  _descriptor.MethodDescriptor(
    name='UpdateDataBundle',
    full_name='Controllable.UpdateDataBundle',
    index=0,
    containing_service=None,
    input_type=protos_dot_data__pb2._DATA,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateParameters',
    full_name='Controllable.UpdateParameters',
    index=1,
    containing_service=None,
    input_type=protos_dot_controller__pb2._PARAMETERSUPDATEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Initialize',
    full_name='Controllable.Initialize',
    index=2,
    containing_service=None,
    input_type=protos_dot_data__pb2._DATA,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClockUpdate',
    full_name='Controllable.ClockUpdate',
    index=3,
    containing_service=None,
    input_type=protos_dot_clock__pb2._CLOCKEVENT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAccount',
    full_name='Controllable.UpdateAccount',
    index=4,
    containing_service=None,
    input_type=protos_dot_data__pb2._DATA,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateCalendar',
    full_name='Controllable.UpdateCalendar',
    index=5,
    containing_service=None,
    input_type=protos_dot_data__pb2._DATA,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Stop',
    full_name='Controllable.Stop',
    index=6,
    containing_service=None,
    input_type=protos_dot_controller__pb2._STOPPARAMS,
    output_type=protos_dot_data__pb2._DATA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLLABLE)

DESCRIPTOR.services_by_name['Controllable'] = _CONTROLLABLE

# @@protoc_insertion_point(module_scope)
