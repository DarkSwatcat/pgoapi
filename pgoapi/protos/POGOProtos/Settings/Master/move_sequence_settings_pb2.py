# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/move_sequence_settings.proto

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
  name='pogoprotos/settings/master/move_sequence_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n7pogoprotos/settings/master/move_sequence_settings.proto\x12\x1apogoprotos.settings.master\"(\n\x14MoveSequenceSettings\x12\x10\n\x08sequence\x18\x01 \x03(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MOVESEQUENCESETTINGS = _descriptor.Descriptor(
  name='MoveSequenceSettings',
  full_name='pogoprotos.settings.master.MoveSequenceSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence', full_name='pogoprotos.settings.master.MoveSequenceSettings.sequence', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=87,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['MoveSequenceSettings'] = _MOVESEQUENCESETTINGS

MoveSequenceSettings = _reflection.GeneratedProtocolMessageType('MoveSequenceSettings', (_message.Message,), dict(
  DESCRIPTOR = _MOVESEQUENCESETTINGS,
  __module__ = 'pogoprotos.settings.master.move_sequence_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.MoveSequenceSettings)
  ))
_sym_db.RegisterMessage(MoveSequenceSettings)


# @@protoc_insertion_point(module_scope)
