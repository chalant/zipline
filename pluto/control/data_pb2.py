# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contrib/control/data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contrib/control/data.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x63ontrib/control/data.proto\"\x14\n\x04\x44\x61ta\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x62\x06proto3')
)




_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Data.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=30,
  serialized_end=50,
)

DESCRIPTOR.message_types_by_name['Data'] = _DATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
  DESCRIPTOR = _DATA,
  __module__ = 'contrib.control.data_pb2'
  # @@protoc_insertion_point(class_scope:Data)
  ))
_sym_db.RegisterMessage(Data)


# @@protoc_insertion_point(module_scope)
