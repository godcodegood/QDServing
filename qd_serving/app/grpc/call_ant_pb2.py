# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: call_ant.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='call_ant.proto',
  package='callant',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x63\x61ll_ant.proto\x12\x07\x63\x61llant\"\x1a\n\nAntRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n\x08\x41ntReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t2?\n\x07Greeter\x12\x34\n\x08SendData\x12\x13.callant.AntRequest\x1a\x11.callant.AntReply\"\x00\x42\x30\n\x18io.grpc.examples.callantB\x0c\x43\x61llAntProtoP\x01\xa2\x02\x03\x61ntb\x06proto3')
)




_ANTREQUEST = _descriptor.Descriptor(
  name='AntRequest',
  full_name='callant.AntRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='callant.AntRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=53,
)


_ANTREPLY = _descriptor.Descriptor(
  name='AntReply',
  full_name='callant.AntReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='callant.AntReply.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='callant.AntReply.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['AntRequest'] = _ANTREQUEST
DESCRIPTOR.message_types_by_name['AntReply'] = _ANTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AntRequest = _reflection.GeneratedProtocolMessageType('AntRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANTREQUEST,
  __module__ = 'call_ant_pb2'
  # @@protoc_insertion_point(class_scope:callant.AntRequest)
  ))
_sym_db.RegisterMessage(AntRequest)

AntReply = _reflection.GeneratedProtocolMessageType('AntReply', (_message.Message,), dict(
  DESCRIPTOR = _ANTREPLY,
  __module__ = 'call_ant_pb2'
  # @@protoc_insertion_point(class_scope:callant.AntReply)
  ))
_sym_db.RegisterMessage(AntReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030io.grpc.examples.callantB\014CallAntProtoP\001\242\002\003ant'))

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='callant.Greeter',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=95,
  serialized_end=158,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendData',
    full_name='callant.Greeter.SendData',
    index=0,
    containing_service=None,
    input_type=_ANTREQUEST,
    output_type=_ANTREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
