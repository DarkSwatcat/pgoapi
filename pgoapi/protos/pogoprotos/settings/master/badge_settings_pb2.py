# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/badge_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import badge_type_pb2 as pogoprotos_dot_enums_dot_badge__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/badge_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n/pogoprotos/settings/master/badge_settings.proto\x12\x1apogoprotos.settings.master\x1a!pogoprotos/enums/badge_type.proto\"e\n\rBadgeSettings\x12/\n\nbadge_type\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.BadgeType\x12\x12\n\nbadge_rank\x18\x02 \x01(\x05\x12\x0f\n\x07targets\x18\x03 \x03(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_badge__type__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BADGESETTINGS = _descriptor.Descriptor(
  name='BadgeSettings',
  full_name='pogoprotos.settings.master.BadgeSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='badge_type', full_name='pogoprotos.settings.master.BadgeSettings.badge_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='badge_rank', full_name='pogoprotos.settings.master.BadgeSettings.badge_rank', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='targets', full_name='pogoprotos.settings.master.BadgeSettings.targets', index=2,
      number=3, type=5, cpp_type=1, label=3,
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
  serialized_start=114,
  serialized_end=215,
)

_BADGESETTINGS.fields_by_name['badge_type'].enum_type = pogoprotos_dot_enums_dot_badge__type__pb2._BADGETYPE
DESCRIPTOR.message_types_by_name['BadgeSettings'] = _BADGESETTINGS

BadgeSettings = _reflection.GeneratedProtocolMessageType('BadgeSettings', (_message.Message,), dict(
  DESCRIPTOR = _BADGESETTINGS,
  __module__ = 'pogoprotos.settings.master.badge_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.BadgeSettings)
  ))
_sym_db.RegisterMessage(BadgeSettings)


# @@protoc_insertion_point(module_scope)