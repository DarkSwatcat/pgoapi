# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import tutorial_state_pb2 as pogoprotos_dot_enums_dot_tutorial__state__pb2
from pogoprotos.data.player import player_avatar_pb2 as pogoprotos_dot_data_dot_player_dot_player__avatar__pb2
from pogoprotos.data.player import daily_bonus_pb2 as pogoprotos_dot_data_dot_player_dot_daily__bonus__pb2
from pogoprotos.data.player import equipped_badge_pb2 as pogoprotos_dot_data_dot_player_dot_equipped__badge__pb2
from pogoprotos.data.player import contact_settings_pb2 as pogoprotos_dot_data_dot_player_dot_contact__settings__pb2
from pogoprotos.data.player import currency_pb2 as pogoprotos_dot_data_dot_player_dot_currency__pb2
from pogoprotos.enums import team_color_pb2 as pogoprotos_dot_enums_dot_team__color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player_data.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_pb=_b('\n!pogoprotos/data/player_data.proto\x12\x0fpogoprotos.data\x1a%pogoprotos/enums/tutorial_state.proto\x1a*pogoprotos/data/player/player_avatar.proto\x1a(pogoprotos/data/player/daily_bonus.proto\x1a+pogoprotos/data/player/equipped_badge.proto\x1a-pogoprotos/data/player/contact_settings.proto\x1a%pogoprotos/data/player/currency.proto\x1a!pogoprotos/enums/team_color.proto\"\xa6\x04\n\nPlayerData\x12\x1d\n\x15\x63reation_timestamp_ms\x18\x01 \x01(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12)\n\x04team\x18\x05 \x01(\x0e\x32\x1b.pogoprotos.enums.TeamColor\x12;\n\x0etutorial_state\x18\x07 \x03(\x0e\x32\x1f.pogoprotos.enums.TutorialStateB\x02\x10\x01\x12\x34\n\x06\x61vatar\x18\x08 \x01(\x0b\x32$.pogoprotos.data.player.PlayerAvatar\x12\x1b\n\x13max_pokemon_storage\x18\t \x01(\x05\x12\x18\n\x10max_item_storage\x18\n \x01(\x05\x12\x37\n\x0b\x64\x61ily_bonus\x18\x0b \x01(\x0b\x32\".pogoprotos.data.player.DailyBonus\x12=\n\x0e\x65quipped_badge\x18\x0c \x01(\x0b\x32%.pogoprotos.data.player.EquippedBadge\x12\x41\n\x10\x63ontact_settings\x18\r \x01(\x0b\x32\'.pogoprotos.data.player.ContactSettings\x12\x34\n\ncurrencies\x18\x0e \x03(\x0b\x32 .pogoprotos.data.player.Currency\x12!\n\x19remaining_codename_claims\x18\x0f \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_tutorial__state__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__avatar__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_daily__bonus__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_equipped__badge__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_contact__settings__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_currency__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_team__color__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLAYERDATA = _descriptor.Descriptor(
  name='PlayerData',
  full_name='pogoprotos.data.PlayerData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creation_timestamp_ms', full_name='pogoprotos.data.PlayerData.creation_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='pogoprotos.data.PlayerData.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team', full_name='pogoprotos.data.PlayerData.team', index=2,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tutorial_state', full_name='pogoprotos.data.PlayerData.tutorial_state', index=3,
      number=7, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='pogoprotos.data.PlayerData.avatar', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_pokemon_storage', full_name='pogoprotos.data.PlayerData.max_pokemon_storage', index=5,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_item_storage', full_name='pogoprotos.data.PlayerData.max_item_storage', index=6,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_bonus', full_name='pogoprotos.data.PlayerData.daily_bonus', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipped_badge', full_name='pogoprotos.data.PlayerData.equipped_badge', index=8,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contact_settings', full_name='pogoprotos.data.PlayerData.contact_settings', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currencies', full_name='pogoprotos.data.PlayerData.currencies', index=10,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remaining_codename_claims', full_name='pogoprotos.data.PlayerData.remaining_codename_claims', index=11,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=346,
  serialized_end=896,
)

_PLAYERDATA.fields_by_name['team'].enum_type = pogoprotos_dot_enums_dot_team__color__pb2._TEAMCOLOR
_PLAYERDATA.fields_by_name['tutorial_state'].enum_type = pogoprotos_dot_enums_dot_tutorial__state__pb2._TUTORIALSTATE
_PLAYERDATA.fields_by_name['avatar'].message_type = pogoprotos_dot_data_dot_player_dot_player__avatar__pb2._PLAYERAVATAR
_PLAYERDATA.fields_by_name['daily_bonus'].message_type = pogoprotos_dot_data_dot_player_dot_daily__bonus__pb2._DAILYBONUS
_PLAYERDATA.fields_by_name['equipped_badge'].message_type = pogoprotos_dot_data_dot_player_dot_equipped__badge__pb2._EQUIPPEDBADGE
_PLAYERDATA.fields_by_name['contact_settings'].message_type = pogoprotos_dot_data_dot_player_dot_contact__settings__pb2._CONTACTSETTINGS
_PLAYERDATA.fields_by_name['currencies'].message_type = pogoprotos_dot_data_dot_player_dot_currency__pb2._CURRENCY
DESCRIPTOR.message_types_by_name['PlayerData'] = _PLAYERDATA

PlayerData = _reflection.GeneratedProtocolMessageType('PlayerData', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERDATA,
  __module__ = 'pogoprotos.data.player_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.PlayerData)
  ))
_sym_db.RegisterMessage(PlayerData)


_PLAYERDATA.fields_by_name['tutorial_state'].has_options = True
_PLAYERDATA.fields_by_name['tutorial_state']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)