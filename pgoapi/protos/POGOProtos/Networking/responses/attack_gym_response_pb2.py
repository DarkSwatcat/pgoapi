# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/attack_gym_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.battle import battle_log_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__log__pb2
from pogoprotos.data.battle import battle_pokemon_info_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/attack_gym_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n9pogoprotos/networking/responses/attack_gym_response.proto\x12\x1fpogoprotos.networking.responses\x1a\'pogoprotos/data/battle/battle_log.proto\x1a\x30pogoprotos/data/battle/battle_pokemon_info.proto\"\x8c\x03\n\x11\x41ttackGymResponse\x12I\n\x06result\x18\x01 \x01(\x0e\x32\x39.pogoprotos.networking.responses.AttackGymResponse.Result\x12\x35\n\nbattle_log\x18\x02 \x01(\x0b\x32!.pogoprotos.data.battle.BattleLog\x12\x11\n\tbattle_id\x18\x03 \x01(\t\x12\x42\n\x0f\x61\x63tive_defender\x18\x04 \x01(\x0b\x32).pogoprotos.data.battle.BattlePokemonInfo\x12\x42\n\x0f\x61\x63tive_attacker\x18\x05 \x01(\x0b\x32).pogoprotos.data.battle.BattlePokemonInfo\"Z\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12 \n\x1c\x45RROR_INVALID_ATTACK_ACTIONS\x10\x02\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_battle_dot_battle__log__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ATTACKGYMRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.AttackGymResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_ATTACK_ACTIONS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IN_RANGE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=492,
  serialized_end=582,
)
_sym_db.RegisterEnumDescriptor(_ATTACKGYMRESPONSE_RESULT)


_ATTACKGYMRESPONSE = _descriptor.Descriptor(
  name='AttackGymResponse',
  full_name='pogoprotos.networking.responses.AttackGymResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.AttackGymResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_log', full_name='pogoprotos.networking.responses.AttackGymResponse.battle_log', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_id', full_name='pogoprotos.networking.responses.AttackGymResponse.battle_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_defender', full_name='pogoprotos.networking.responses.AttackGymResponse.active_defender', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_attacker', full_name='pogoprotos.networking.responses.AttackGymResponse.active_attacker', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ATTACKGYMRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=582,
)

_ATTACKGYMRESPONSE.fields_by_name['result'].enum_type = _ATTACKGYMRESPONSE_RESULT
_ATTACKGYMRESPONSE.fields_by_name['battle_log'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__log__pb2._BATTLELOG
_ATTACKGYMRESPONSE.fields_by_name['active_defender'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2._BATTLEPOKEMONINFO
_ATTACKGYMRESPONSE.fields_by_name['active_attacker'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2._BATTLEPOKEMONINFO
_ATTACKGYMRESPONSE_RESULT.containing_type = _ATTACKGYMRESPONSE
DESCRIPTOR.message_types_by_name['AttackGymResponse'] = _ATTACKGYMRESPONSE

AttackGymResponse = _reflection.GeneratedProtocolMessageType('AttackGymResponse', (_message.Message,), dict(
  DESCRIPTOR = _ATTACKGYMRESPONSE,
  __module__ = 'pogoprotos.networking.responses.attack_gym_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.AttackGymResponse)
  ))
_sym_db.RegisterMessage(AttackGymResponse)


# @@protoc_insertion_point(module_scope)
