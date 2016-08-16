# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/global_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings import fort_settings_pb2 as pogoprotos_dot_settings_dot_fort__settings__pb2
from pogoprotos.settings import map_settings_pb2 as pogoprotos_dot_settings_dot_map__settings__pb2
from pogoprotos.settings import level_settings_pb2 as pogoprotos_dot_settings_dot_level__settings__pb2
from pogoprotos.settings import inventory_settings_pb2 as pogoprotos_dot_settings_dot_inventory__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/settings/global_settings.proto\x12\x13pogoprotos.settings\x1a\'pogoprotos/settings/fort_settings.proto\x1a&pogoprotos/settings/map_settings.proto\x1a(pogoprotos/settings/level_settings.proto\x1a,pogoprotos/settings/inventory_settings.proto\"\xa2\x02\n\x0eGlobalSettings\x12\x38\n\rfort_settings\x18\x02 \x01(\x0b\x32!.pogoprotos.settings.FortSettings\x12\x36\n\x0cmap_settings\x18\x03 \x01(\x0b\x32 .pogoprotos.settings.MapSettings\x12:\n\x0elevel_settings\x18\x04 \x01(\x0b\x32\".pogoprotos.settings.LevelSettings\x12\x42\n\x12inventory_settings\x18\x05 \x01(\x0b\x32&.pogoprotos.settings.InventorySettings\x12\x1e\n\x16minimum_client_version\x18\x06 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_settings_dot_fort__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_map__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_level__settings__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_inventory__settings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GLOBALSETTINGS = _descriptor.Descriptor(
  name='GlobalSettings',
  full_name='pogoprotos.settings.GlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_settings', full_name='pogoprotos.settings.GlobalSettings.fort_settings', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_settings', full_name='pogoprotos.settings.GlobalSettings.map_settings', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_settings', full_name='pogoprotos.settings.GlobalSettings.level_settings', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_settings', full_name='pogoprotos.settings.GlobalSettings.inventory_settings', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum_client_version', full_name='pogoprotos.settings.GlobalSettings.minimum_client_version', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=236,
  serialized_end=526,
)

_GLOBALSETTINGS.fields_by_name['fort_settings'].message_type = pogoprotos_dot_settings_dot_fort__settings__pb2._FORTSETTINGS
_GLOBALSETTINGS.fields_by_name['map_settings'].message_type = pogoprotos_dot_settings_dot_map__settings__pb2._MAPSETTINGS
_GLOBALSETTINGS.fields_by_name['level_settings'].message_type = pogoprotos_dot_settings_dot_level__settings__pb2._LEVELSETTINGS
_GLOBALSETTINGS.fields_by_name['inventory_settings'].message_type = pogoprotos_dot_settings_dot_inventory__settings__pb2._INVENTORYSETTINGS
DESCRIPTOR.message_types_by_name['GlobalSettings'] = _GLOBALSETTINGS

GlobalSettings = _reflection.GeneratedProtocolMessageType('GlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALSETTINGS,
  __module__ = 'pogoprotos.settings.global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.GlobalSettings)
  ))
_sym_db.RegisterMessage(GlobalSettings)


# @@protoc_insertion_point(module_scope)
