# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/catch_pokemon_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/catch_pokemon_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_pb=_b('\n2pogoprotos/data/logs/catch_pokemon_log_entry.proto\x12\x14pogoprotos.data.logs\x1a!pogoprotos/enums/pokemon_id.proto\"\x8c\x02\n\x14\x43\x61tchPokemonLogEntry\x12\x41\n\x06result\x18\x01 \x01(\x0e\x32\x31.pogoprotos.data.logs.CatchPokemonLogEntry.Result\x12/\n\npokemon_id\x18\x02 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x15\n\rcombat_points\x18\x03 \x01(\x05\x12\x17\n\x0fpokemon_data_id\x18\x04 \x01(\x06\"P\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x14\n\x10POKEMON_CAPTURED\x10\x01\x12\x10\n\x0cPOKEMON_FLED\x10\x02\x12\x13\n\x0fPOKEMON_HATCHED\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CATCHPOKEMONLOGENTRY_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.data.logs.CatchPokemonLogEntry.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_CAPTURED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_FLED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_HATCHED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=300,
  serialized_end=380,
)
_sym_db.RegisterEnumDescriptor(_CATCHPOKEMONLOGENTRY_RESULT)


_CATCHPOKEMONLOGENTRY = _descriptor.Descriptor(
  name='CatchPokemonLogEntry',
  full_name='pogoprotos.data.logs.CatchPokemonLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.logs.CatchPokemonLogEntry.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.logs.CatchPokemonLogEntry.pokemon_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_points', full_name='pogoprotos.data.logs.CatchPokemonLogEntry.combat_points', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_data_id', full_name='pogoprotos.data.logs.CatchPokemonLogEntry.pokemon_data_id', index=3,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CATCHPOKEMONLOGENTRY_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=380,
)

_CATCHPOKEMONLOGENTRY.fields_by_name['result'].enum_type = _CATCHPOKEMONLOGENTRY_RESULT
_CATCHPOKEMONLOGENTRY.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_CATCHPOKEMONLOGENTRY_RESULT.containing_type = _CATCHPOKEMONLOGENTRY
DESCRIPTOR.message_types_by_name['CatchPokemonLogEntry'] = _CATCHPOKEMONLOGENTRY

CatchPokemonLogEntry = _reflection.GeneratedProtocolMessageType('CatchPokemonLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _CATCHPOKEMONLOGENTRY,
  __module__ = 'pogoprotos.data.logs.catch_pokemon_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.CatchPokemonLogEntry)
  ))
_sym_db.RegisterMessage(CatchPokemonLogEntry)


# @@protoc_insertion_point(module_scope)
