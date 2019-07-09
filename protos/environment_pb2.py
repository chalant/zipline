# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/environment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import data_bundle_pb2 as protos_dot_data__bundle__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/environment.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18protos/environment.proto\x1a\x18protos/data_bundle.proto\";\n\x15\x43ontrollerEnvironment\x12\"\n\tsess_doms\x18\x01 \x03(\x0b\x32\x0f.SessionsDomain\"D\n\x0fUserEnvironment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x65nvironment\x18\x02 \x01(\x0c\x12\x10\n\x08strategy\x18\x03 \x01(\x0c\"4\n\x13StrategyEnvironment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"H\n\rStrategyGroup\x12&\n\ndomain_def\x18\x01 \x01(\x0b\x32\x12.CompoundDomainDef\x12\x0f\n\x07str_ids\x18\x02 \x03(\t\"<\n\x08HubStore\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x1d\n\x05group\x18\x02 \x01(\x0b\x32\x0e.StrategyGroup\"\'\n\x07Session\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08strategy\x18\x03 \x01(\x0c\"R\n\rSessionDomain\x12&\n\ndomain_def\x18\x01 \x01(\x0b\x32\x12.CompoundDomainDef\x12\x19\n\x07session\x18\x02 \x01(\x0b\x32\x08.Session\"T\n\x0eSessionsDomain\x12\x1a\n\x08sessions\x18\x01 \x03(\x0b\x32\x08.Session\x12&\n\ndomain_def\x18\x02 \x01(\x0b\x32\x12.CompoundDomainDefb\x06proto3')
  ,
  dependencies=[protos_dot_data__bundle__pb2.DESCRIPTOR,])




_CONTROLLERENVIRONMENT = _descriptor.Descriptor(
  name='ControllerEnvironment',
  full_name='ControllerEnvironment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sess_doms', full_name='ControllerEnvironment.sess_doms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=54,
  serialized_end=113,
)


_USERENVIRONMENT = _descriptor.Descriptor(
  name='UserEnvironment',
  full_name='UserEnvironment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UserEnvironment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environment', full_name='UserEnvironment.environment', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='UserEnvironment.strategy', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=115,
  serialized_end=183,
)


_STRATEGYENVIRONMENT = _descriptor.Descriptor(
  name='StrategyEnvironment',
  full_name='StrategyEnvironment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='StrategyEnvironment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='StrategyEnvironment.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=185,
  serialized_end=237,
)


_STRATEGYGROUP = _descriptor.Descriptor(
  name='StrategyGroup',
  full_name='StrategyGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_def', full_name='StrategyGroup.domain_def', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str_ids', full_name='StrategyGroup.str_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=239,
  serialized_end=311,
)


_HUBSTORE = _descriptor.Descriptor(
  name='HubStore',
  full_name='HubStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='HubStore.domain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='HubStore.group', index=1,
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
  serialized_start=313,
  serialized_end=373,
)


_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Session.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='Session.strategy', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=375,
  serialized_end=414,
)


_SESSIONDOMAIN = _descriptor.Descriptor(
  name='SessionDomain',
  full_name='SessionDomain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_def', full_name='SessionDomain.domain_def', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session', full_name='SessionDomain.session', index=1,
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
  serialized_start=416,
  serialized_end=498,
)


_SESSIONSDOMAIN = _descriptor.Descriptor(
  name='SessionsDomain',
  full_name='SessionsDomain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sessions', full_name='SessionsDomain.sessions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_def', full_name='SessionsDomain.domain_def', index=1,
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
  serialized_start=500,
  serialized_end=584,
)

_CONTROLLERENVIRONMENT.fields_by_name['sess_doms'].message_type = _SESSIONSDOMAIN
_STRATEGYGROUP.fields_by_name['domain_def'].message_type = protos_dot_data__bundle__pb2._COMPOUNDDOMAINDEF
_HUBSTORE.fields_by_name['group'].message_type = _STRATEGYGROUP
_SESSIONDOMAIN.fields_by_name['domain_def'].message_type = protos_dot_data__bundle__pb2._COMPOUNDDOMAINDEF
_SESSIONDOMAIN.fields_by_name['session'].message_type = _SESSION
_SESSIONSDOMAIN.fields_by_name['sessions'].message_type = _SESSION
_SESSIONSDOMAIN.fields_by_name['domain_def'].message_type = protos_dot_data__bundle__pb2._COMPOUNDDOMAINDEF
DESCRIPTOR.message_types_by_name['ControllerEnvironment'] = _CONTROLLERENVIRONMENT
DESCRIPTOR.message_types_by_name['UserEnvironment'] = _USERENVIRONMENT
DESCRIPTOR.message_types_by_name['StrategyEnvironment'] = _STRATEGYENVIRONMENT
DESCRIPTOR.message_types_by_name['StrategyGroup'] = _STRATEGYGROUP
DESCRIPTOR.message_types_by_name['HubStore'] = _HUBSTORE
DESCRIPTOR.message_types_by_name['Session'] = _SESSION
DESCRIPTOR.message_types_by_name['SessionDomain'] = _SESSIONDOMAIN
DESCRIPTOR.message_types_by_name['SessionsDomain'] = _SESSIONSDOMAIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControllerEnvironment = _reflection.GeneratedProtocolMessageType('ControllerEnvironment', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLLERENVIRONMENT,
  __module__ = 'protos.environment_pb2'
  # @@protoc_insertion_point(class_scope:ControllerEnvironment)
  ))
_sym_db.RegisterMessage(ControllerEnvironment)

UserEnvironment = _reflection.GeneratedProtocolMessageType('UserEnvironment', (_message.Message,), dict(
  DESCRIPTOR = _USERENVIRONMENT,
  __module__ = 'protos.environment_pb2'
  # @@protoc_insertion_point(class_scope:UserEnvironment)
  ))
_sym_db.RegisterMessage(UserEnvironment)

StrategyEnvironment = _reflection.GeneratedProtocolMessageType('StrategyEnvironment', (_message.Message,), dict(
  DESCRIPTOR = _STRATEGYENVIRONMENT,
  __module__ = 'protos.environment_pb2'
  # @@protoc_insertion_point(class_scope:StrategyEnvironment)
  ))
_sym_db.RegisterMessage(StrategyEnvironment)

StrategyGroup = _reflection.GeneratedProtocolMessageType('StrategyGroup', (_message.Message,), dict(
  DESCRIPTOR = _STRATEGYGROUP,
  __module__ = 'protos.environment_pb2'
  # @@protoc_insertion_point(class_scope:StrategyGroup)
  ))
_sym_db.RegisterMessage(StrategyGroup)

HubStore = _reflection.GeneratedProtocolMessageType('HubStore', (_message.Message,), dict(
  DESCRIPTOR = _HUBSTORE,
  __module__ = 'protos.environment_pb2'
  # @@protoc_insertion_point(class_scope:HubStore)
  ))
_sym_db.RegisterMessage(HubStore)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), dict(
  DESCRIPTOR = _SESSION,
  __module__ = 'protos.environment_pb2'
  # @@protoc_insertion_point(class_scope:Session)
  ))
_sym_db.RegisterMessage(Session)

SessionDomain = _reflection.GeneratedProtocolMessageType('SessionDomain', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONDOMAIN,
  __module__ = 'protos.environment_pb2'
  # @@protoc_insertion_point(class_scope:SessionDomain)
  ))
_sym_db.RegisterMessage(SessionDomain)

SessionsDomain = _reflection.GeneratedProtocolMessageType('SessionsDomain', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONSDOMAIN,
  __module__ = 'protos.environment_pb2'
  # @@protoc_insertion_point(class_scope:SessionsDomain)
  ))
_sym_db.RegisterMessage(SessionsDomain)


# @@protoc_insertion_point(module_scope)
