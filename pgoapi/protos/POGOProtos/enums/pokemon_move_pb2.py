# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/pokemon_move.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/pokemon_move.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n#pogoprotos/enums/pokemon_move.proto\x12\x10pogoprotos.enums*\xce\x17\n\x0bPokemonMove\x12\x0e\n\nMOVE_UNSET\x10\x00\x12\x11\n\rTHUNDER_SHOCK\x10\x01\x12\x10\n\x0cQUICK_ATTACK\x10\x02\x12\x0b\n\x07SCRATCH\x10\x03\x12\t\n\x05\x45MBER\x10\x04\x12\r\n\tVINE_WHIP\x10\x05\x12\n\n\x06TACKLE\x10\x06\x12\x0e\n\nRAZOR_LEAF\x10\x07\x12\r\n\tTAKE_DOWN\x10\x08\x12\r\n\tWATER_GUN\x10\t\x12\x08\n\x04\x42ITE\x10\n\x12\t\n\x05POUND\x10\x0b\x12\x0f\n\x0b\x44OUBLE_SLAP\x10\x0c\x12\x08\n\x04WRAP\x10\r\x12\x0e\n\nHYPER_BEAM\x10\x0e\x12\x08\n\x04LICK\x10\x0f\x12\x0e\n\nDARK_PULSE\x10\x10\x12\x08\n\x04SMOG\x10\x11\x12\n\n\x06SLUDGE\x10\x12\x12\x0e\n\nMETAL_CLAW\x10\x13\x12\r\n\tVICE_GRIP\x10\x14\x12\x0f\n\x0b\x46LAME_WHEEL\x10\x15\x12\x0c\n\x08MEGAHORN\x10\x16\x12\x0f\n\x0bWING_ATTACK\x10\x17\x12\x10\n\x0c\x46LAMETHROWER\x10\x18\x12\x10\n\x0cSUCKER_PUNCH\x10\x19\x12\x07\n\x03\x44IG\x10\x1a\x12\x0c\n\x08LOW_KICK\x10\x1b\x12\x0e\n\nCROSS_CHOP\x10\x1c\x12\x0e\n\nPSYCHO_CUT\x10\x1d\x12\x0b\n\x07PSYBEAM\x10\x1e\x12\x0e\n\nEARTHQUAKE\x10\x1f\x12\x0e\n\nSTONE_EDGE\x10 \x12\r\n\tICE_PUNCH\x10!\x12\x0f\n\x0bHEART_STAMP\x10\"\x12\r\n\tDISCHARGE\x10#\x12\x10\n\x0c\x46LASH_CANNON\x10$\x12\x08\n\x04PECK\x10%\x12\x0e\n\nDRILL_PECK\x10&\x12\x0c\n\x08ICE_BEAM\x10\'\x12\x0c\n\x08\x42LIZZARD\x10(\x12\r\n\tAIR_SLASH\x10)\x12\r\n\tHEAT_WAVE\x10*\x12\r\n\tTWINEEDLE\x10+\x12\x0e\n\nPOISON_JAB\x10,\x12\x0e\n\nAERIAL_ACE\x10-\x12\r\n\tDRILL_RUN\x10.\x12\x12\n\x0ePETAL_BLIZZARD\x10/\x12\x0e\n\nMEGA_DRAIN\x10\x30\x12\x0c\n\x08\x42UG_BUZZ\x10\x31\x12\x0f\n\x0bPOISON_FANG\x10\x32\x12\x0f\n\x0bNIGHT_SLASH\x10\x33\x12\t\n\x05SLASH\x10\x34\x12\x0f\n\x0b\x42UBBLE_BEAM\x10\x35\x12\x0e\n\nSUBMISSION\x10\x36\x12\x0f\n\x0bKARATE_CHOP\x10\x37\x12\r\n\tLOW_SWEEP\x10\x38\x12\x0c\n\x08\x41QUA_JET\x10\x39\x12\r\n\tAQUA_TAIL\x10:\x12\r\n\tSEED_BOMB\x10;\x12\x0c\n\x08PSYSHOCK\x10<\x12\x0e\n\nROCK_THROW\x10=\x12\x11\n\rANCIENT_POWER\x10>\x12\r\n\tROCK_TOMB\x10?\x12\x0e\n\nROCK_SLIDE\x10@\x12\r\n\tPOWER_GEM\x10\x41\x12\x10\n\x0cSHADOW_SNEAK\x10\x42\x12\x10\n\x0cSHADOW_PUNCH\x10\x43\x12\x0f\n\x0bSHADOW_CLAW\x10\x44\x12\x10\n\x0cOMINOUS_WIND\x10\x45\x12\x0f\n\x0bSHADOW_BALL\x10\x46\x12\x10\n\x0c\x42ULLET_PUNCH\x10G\x12\x0f\n\x0bMAGNET_BOMB\x10H\x12\x0e\n\nSTEEL_WING\x10I\x12\r\n\tIRON_HEAD\x10J\x12\x14\n\x10PARABOLIC_CHARGE\x10K\x12\t\n\x05SPARK\x10L\x12\x11\n\rTHUNDER_PUNCH\x10M\x12\x0b\n\x07THUNDER\x10N\x12\x0f\n\x0bTHUNDERBOLT\x10O\x12\x0b\n\x07TWISTER\x10P\x12\x11\n\rDRAGON_BREATH\x10Q\x12\x10\n\x0c\x44RAGON_PULSE\x10R\x12\x0f\n\x0b\x44RAGON_CLAW\x10S\x12\x13\n\x0f\x44ISARMING_VOICE\x10T\x12\x11\n\rDRAINING_KISS\x10U\x12\x12\n\x0e\x44\x41ZZLING_GLEAM\x10V\x12\r\n\tMOONBLAST\x10W\x12\x0e\n\nPLAY_ROUGH\x10X\x12\x10\n\x0c\x43ROSS_POISON\x10Y\x12\x0f\n\x0bSLUDGE_BOMB\x10Z\x12\x0f\n\x0bSLUDGE_WAVE\x10[\x12\r\n\tGUNK_SHOT\x10\\\x12\x0c\n\x08MUD_SHOT\x10]\x12\r\n\tBONE_CLUB\x10^\x12\x0c\n\x08\x42ULLDOZE\x10_\x12\x0c\n\x08MUD_BOMB\x10`\x12\x0f\n\x0b\x46URY_CUTTER\x10\x61\x12\x0c\n\x08\x42UG_BITE\x10\x62\x12\x0f\n\x0bSIGNAL_BEAM\x10\x63\x12\r\n\tX_SCISSOR\x10\x64\x12\x10\n\x0c\x46LAME_CHARGE\x10\x65\x12\x0f\n\x0b\x46LAME_BURST\x10\x66\x12\x0e\n\nFIRE_BLAST\x10g\x12\t\n\x05\x42RINE\x10h\x12\x0f\n\x0bWATER_PULSE\x10i\x12\t\n\x05SCALD\x10j\x12\x0e\n\nHYDRO_PUMP\x10k\x12\x0b\n\x07PSYCHIC\x10l\x12\r\n\tPSYSTRIKE\x10m\x12\r\n\tICE_SHARD\x10n\x12\x0c\n\x08ICY_WIND\x10o\x12\x10\n\x0c\x46ROST_BREATH\x10p\x12\n\n\x06\x41\x42SORB\x10q\x12\x0e\n\nGIGA_DRAIN\x10r\x12\x0e\n\nFIRE_PUNCH\x10s\x12\x0e\n\nSOLAR_BEAM\x10t\x12\x0e\n\nLEAF_BLADE\x10u\x12\x0e\n\nPOWER_WHIP\x10v\x12\n\n\x06SPLASH\x10w\x12\x08\n\x04\x41\x43ID\x10x\x12\x0e\n\nAIR_CUTTER\x10y\x12\r\n\tHURRICANE\x10z\x12\x0f\n\x0b\x42RICK_BREAK\x10{\x12\x07\n\x03\x43UT\x10|\x12\t\n\x05SWIFT\x10}\x12\x0f\n\x0bHORN_ATTACK\x10~\x12\t\n\x05STOMP\x10\x7f\x12\r\n\x08HEADBUTT\x10\x80\x01\x12\x0f\n\nHYPER_FANG\x10\x81\x01\x12\t\n\x04SLAM\x10\x82\x01\x12\x0e\n\tBODY_SLAM\x10\x83\x01\x12\t\n\x04REST\x10\x84\x01\x12\r\n\x08STRUGGLE\x10\x85\x01\x12\x14\n\x0fSCALD_BLASTOISE\x10\x86\x01\x12\x19\n\x14HYDRO_PUMP_BLASTOISE\x10\x87\x01\x12\x0f\n\nWRAP_GREEN\x10\x88\x01\x12\x0e\n\tWRAP_PINK\x10\x89\x01\x12\x15\n\x10\x46URY_CUTTER_FAST\x10\xc8\x01\x12\x12\n\rBUG_BITE_FAST\x10\xc9\x01\x12\x0e\n\tBITE_FAST\x10\xca\x01\x12\x16\n\x11SUCKER_PUNCH_FAST\x10\xcb\x01\x12\x17\n\x12\x44RAGON_BREATH_FAST\x10\xcc\x01\x12\x17\n\x12THUNDER_SHOCK_FAST\x10\xcd\x01\x12\x0f\n\nSPARK_FAST\x10\xce\x01\x12\x12\n\rLOW_KICK_FAST\x10\xcf\x01\x12\x15\n\x10KARATE_CHOP_FAST\x10\xd0\x01\x12\x0f\n\nEMBER_FAST\x10\xd1\x01\x12\x15\n\x10WING_ATTACK_FAST\x10\xd2\x01\x12\x0e\n\tPECK_FAST\x10\xd3\x01\x12\x0e\n\tLICK_FAST\x10\xd4\x01\x12\x15\n\x10SHADOW_CLAW_FAST\x10\xd5\x01\x12\x13\n\x0eVINE_WHIP_FAST\x10\xd6\x01\x12\x14\n\x0fRAZOR_LEAF_FAST\x10\xd7\x01\x12\x12\n\rMUD_SHOT_FAST\x10\xd8\x01\x12\x13\n\x0eICE_SHARD_FAST\x10\xd9\x01\x12\x16\n\x11\x46ROST_BREATH_FAST\x10\xda\x01\x12\x16\n\x11QUICK_ATTACK_FAST\x10\xdb\x01\x12\x11\n\x0cSCRATCH_FAST\x10\xdc\x01\x12\x10\n\x0bTACKLE_FAST\x10\xdd\x01\x12\x0f\n\nPOUND_FAST\x10\xde\x01\x12\r\n\x08\x43UT_FAST\x10\xdf\x01\x12\x14\n\x0fPOISON_JAB_FAST\x10\xe0\x01\x12\x0e\n\tACID_FAST\x10\xe1\x01\x12\x14\n\x0fPSYCHO_CUT_FAST\x10\xe2\x01\x12\x14\n\x0fROCK_THROW_FAST\x10\xe3\x01\x12\x14\n\x0fMETAL_CLAW_FAST\x10\xe4\x01\x12\x16\n\x11\x42ULLET_PUNCH_FAST\x10\xe5\x01\x12\x13\n\x0eWATER_GUN_FAST\x10\xe6\x01\x12\x10\n\x0bSPLASH_FAST\x10\xe7\x01\x12\x1d\n\x18WATER_GUN_FAST_BLASTOISE\x10\xe8\x01\x12\x12\n\rMUD_SLAP_FAST\x10\xe9\x01\x12\x16\n\x11ZEN_HEADBUTT_FAST\x10\xea\x01\x12\x13\n\x0e\x43ONFUSION_FAST\x10\xeb\x01\x12\x16\n\x11POISON_STING_FAST\x10\xec\x01\x12\x10\n\x0b\x42UBBLE_FAST\x10\xed\x01\x12\x16\n\x11\x46\x45INT_ATTACK_FAST\x10\xee\x01\x12\x14\n\x0fSTEEL_WING_FAST\x10\xef\x01\x12\x13\n\x0e\x46IRE_FANG_FAST\x10\xf0\x01\x12\x14\n\x0fROCK_SMASH_FAST\x10\xf1\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_POKEMONMOVE = _descriptor.EnumDescriptor(
  name='PokemonMove',
  full_name='pogoprotos.enums.PokemonMove',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOVE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THUNDER_SHOCK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUICK_ATTACK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCRATCH', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMBER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VINE_WHIP', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TACKLE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAZOR_LEAF', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TAKE_DOWN', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WATER_GUN', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BITE', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POUND', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE_SLAP', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRAP', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYPER_BEAM', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LICK', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DARK_PULSE', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SMOG', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLUDGE', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='METAL_CLAW', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VICE_GRIP', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAME_WHEEL', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEGAHORN', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WING_ATTACK', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAMETHROWER', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCKER_PUNCH', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIG', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW_KICK', index=27, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CROSS_CHOP', index=28, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSYCHO_CUT', index=29, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSYBEAM', index=30, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EARTHQUAKE', index=31, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STONE_EDGE', index=32, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICE_PUNCH', index=33, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEART_STAMP', index=34, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCHARGE', index=35, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_CANNON', index=36, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PECK', index=37, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRILL_PECK', index=38, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICE_BEAM', index=39, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLIZZARD', index=40, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AIR_SLASH', index=41, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEAT_WAVE', index=42, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWINEEDLE', index=43, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POISON_JAB', index=44, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AERIAL_ACE', index=45, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRILL_RUN', index=46, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PETAL_BLIZZARD', index=47, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEGA_DRAIN', index=48, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUG_BUZZ', index=49, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POISON_FANG', index=50, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NIGHT_SLASH', index=51, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLASH', index=52, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUBBLE_BEAM', index=53, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMISSION', index=54, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KARATE_CHOP', index=55, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW_SWEEP', index=56, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AQUA_JET', index=57, number=57,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AQUA_TAIL', index=58, number=58,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEED_BOMB', index=59, number=59,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSYSHOCK', index=60, number=60,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROCK_THROW', index=61, number=61,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANCIENT_POWER', index=62, number=62,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROCK_TOMB', index=63, number=63,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROCK_SLIDE', index=64, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POWER_GEM', index=65, number=65,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHADOW_SNEAK', index=66, number=66,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHADOW_PUNCH', index=67, number=67,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHADOW_CLAW', index=68, number=68,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OMINOUS_WIND', index=69, number=69,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHADOW_BALL', index=70, number=70,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BULLET_PUNCH', index=71, number=71,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAGNET_BOMB', index=72, number=72,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STEEL_WING', index=73, number=73,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IRON_HEAD', index=74, number=74,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARABOLIC_CHARGE', index=75, number=75,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPARK', index=76, number=76,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THUNDER_PUNCH', index=77, number=77,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THUNDER', index=78, number=78,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THUNDERBOLT', index=79, number=79,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWISTER', index=80, number=80,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRAGON_BREATH', index=81, number=81,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRAGON_PULSE', index=82, number=82,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRAGON_CLAW', index=83, number=83,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISARMING_VOICE', index=84, number=84,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRAINING_KISS', index=85, number=85,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DAZZLING_GLEAM', index=86, number=86,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOONBLAST', index=87, number=87,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAY_ROUGH', index=88, number=88,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CROSS_POISON', index=89, number=89,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLUDGE_BOMB', index=90, number=90,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLUDGE_WAVE', index=91, number=91,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GUNK_SHOT', index=92, number=92,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUD_SHOT', index=93, number=93,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BONE_CLUB', index=94, number=94,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BULLDOZE', index=95, number=95,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUD_BOMB', index=96, number=96,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FURY_CUTTER', index=97, number=97,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUG_BITE', index=98, number=98,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGNAL_BEAM', index=99, number=99,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='X_SCISSOR', index=100, number=100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAME_CHARGE', index=101, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAME_BURST', index=102, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRE_BLAST', index=103, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BRINE', index=104, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WATER_PULSE', index=105, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCALD', index=106, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYDRO_PUMP', index=107, number=107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSYCHIC', index=108, number=108,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSYSTRIKE', index=109, number=109,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICE_SHARD', index=110, number=110,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICY_WIND', index=111, number=111,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FROST_BREATH', index=112, number=112,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABSORB', index=113, number=113,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIGA_DRAIN', index=114, number=114,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRE_PUNCH', index=115, number=115,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOLAR_BEAM', index=116, number=116,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAF_BLADE', index=117, number=117,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POWER_WHIP', index=118, number=118,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLASH', index=119, number=119,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACID', index=120, number=120,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AIR_CUTTER', index=121, number=121,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HURRICANE', index=122, number=122,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BRICK_BREAK', index=123, number=123,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUT', index=124, number=124,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIFT', index=125, number=125,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HORN_ATTACK', index=126, number=126,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOMP', index=127, number=127,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEADBUTT', index=128, number=128,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYPER_FANG', index=129, number=129,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLAM', index=130, number=130,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BODY_SLAM', index=131, number=131,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REST', index=132, number=132,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRUGGLE', index=133, number=133,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCALD_BLASTOISE', index=134, number=134,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYDRO_PUMP_BLASTOISE', index=135, number=135,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRAP_GREEN', index=136, number=136,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRAP_PINK', index=137, number=137,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FURY_CUTTER_FAST', index=138, number=200,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUG_BITE_FAST', index=139, number=201,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BITE_FAST', index=140, number=202,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCKER_PUNCH_FAST', index=141, number=203,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRAGON_BREATH_FAST', index=142, number=204,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THUNDER_SHOCK_FAST', index=143, number=205,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPARK_FAST', index=144, number=206,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW_KICK_FAST', index=145, number=207,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KARATE_CHOP_FAST', index=146, number=208,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMBER_FAST', index=147, number=209,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WING_ATTACK_FAST', index=148, number=210,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PECK_FAST', index=149, number=211,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LICK_FAST', index=150, number=212,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHADOW_CLAW_FAST', index=151, number=213,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VINE_WHIP_FAST', index=152, number=214,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAZOR_LEAF_FAST', index=153, number=215,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUD_SHOT_FAST', index=154, number=216,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICE_SHARD_FAST', index=155, number=217,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FROST_BREATH_FAST', index=156, number=218,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUICK_ATTACK_FAST', index=157, number=219,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCRATCH_FAST', index=158, number=220,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TACKLE_FAST', index=159, number=221,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POUND_FAST', index=160, number=222,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUT_FAST', index=161, number=223,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POISON_JAB_FAST', index=162, number=224,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACID_FAST', index=163, number=225,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSYCHO_CUT_FAST', index=164, number=226,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROCK_THROW_FAST', index=165, number=227,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='METAL_CLAW_FAST', index=166, number=228,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BULLET_PUNCH_FAST', index=167, number=229,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WATER_GUN_FAST', index=168, number=230,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLASH_FAST', index=169, number=231,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WATER_GUN_FAST_BLASTOISE', index=170, number=232,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUD_SLAP_FAST', index=171, number=233,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZEN_HEADBUTT_FAST', index=172, number=234,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFUSION_FAST', index=173, number=235,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POISON_STING_FAST', index=174, number=236,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUBBLE_FAST', index=175, number=237,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEINT_ATTACK_FAST', index=176, number=238,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STEEL_WING_FAST', index=177, number=239,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRE_FANG_FAST', index=178, number=240,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROCK_SMASH_FAST', index=179, number=241,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=58,
  serialized_end=3080,
)
_sym_db.RegisterEnumDescriptor(_POKEMONMOVE)

PokemonMove = enum_type_wrapper.EnumTypeWrapper(_POKEMONMOVE)
MOVE_UNSET = 0
THUNDER_SHOCK = 1
QUICK_ATTACK = 2
SCRATCH = 3
EMBER = 4
VINE_WHIP = 5
TACKLE = 6
RAZOR_LEAF = 7
TAKE_DOWN = 8
WATER_GUN = 9
BITE = 10
POUND = 11
DOUBLE_SLAP = 12
WRAP = 13
HYPER_BEAM = 14
LICK = 15
DARK_PULSE = 16
SMOG = 17
SLUDGE = 18
METAL_CLAW = 19
VICE_GRIP = 20
FLAME_WHEEL = 21
MEGAHORN = 22
WING_ATTACK = 23
FLAMETHROWER = 24
SUCKER_PUNCH = 25
DIG = 26
LOW_KICK = 27
CROSS_CHOP = 28
PSYCHO_CUT = 29
PSYBEAM = 30
EARTHQUAKE = 31
STONE_EDGE = 32
ICE_PUNCH = 33
HEART_STAMP = 34
DISCHARGE = 35
FLASH_CANNON = 36
PECK = 37
DRILL_PECK = 38
ICE_BEAM = 39
BLIZZARD = 40
AIR_SLASH = 41
HEAT_WAVE = 42
TWINEEDLE = 43
POISON_JAB = 44
AERIAL_ACE = 45
DRILL_RUN = 46
PETAL_BLIZZARD = 47
MEGA_DRAIN = 48
BUG_BUZZ = 49
POISON_FANG = 50
NIGHT_SLASH = 51
SLASH = 52
BUBBLE_BEAM = 53
SUBMISSION = 54
KARATE_CHOP = 55
LOW_SWEEP = 56
AQUA_JET = 57
AQUA_TAIL = 58
SEED_BOMB = 59
PSYSHOCK = 60
ROCK_THROW = 61
ANCIENT_POWER = 62
ROCK_TOMB = 63
ROCK_SLIDE = 64
POWER_GEM = 65
SHADOW_SNEAK = 66
SHADOW_PUNCH = 67
SHADOW_CLAW = 68
OMINOUS_WIND = 69
SHADOW_BALL = 70
BULLET_PUNCH = 71
MAGNET_BOMB = 72
STEEL_WING = 73
IRON_HEAD = 74
PARABOLIC_CHARGE = 75
SPARK = 76
THUNDER_PUNCH = 77
THUNDER = 78
THUNDERBOLT = 79
TWISTER = 80
DRAGON_BREATH = 81
DRAGON_PULSE = 82
DRAGON_CLAW = 83
DISARMING_VOICE = 84
DRAINING_KISS = 85
DAZZLING_GLEAM = 86
MOONBLAST = 87
PLAY_ROUGH = 88
CROSS_POISON = 89
SLUDGE_BOMB = 90
SLUDGE_WAVE = 91
GUNK_SHOT = 92
MUD_SHOT = 93
BONE_CLUB = 94
BULLDOZE = 95
MUD_BOMB = 96
FURY_CUTTER = 97
BUG_BITE = 98
SIGNAL_BEAM = 99
X_SCISSOR = 100
FLAME_CHARGE = 101
FLAME_BURST = 102
FIRE_BLAST = 103
BRINE = 104
WATER_PULSE = 105
SCALD = 106
HYDRO_PUMP = 107
PSYCHIC = 108
PSYSTRIKE = 109
ICE_SHARD = 110
ICY_WIND = 111
FROST_BREATH = 112
ABSORB = 113
GIGA_DRAIN = 114
FIRE_PUNCH = 115
SOLAR_BEAM = 116
LEAF_BLADE = 117
POWER_WHIP = 118
SPLASH = 119
ACID = 120
AIR_CUTTER = 121
HURRICANE = 122
BRICK_BREAK = 123
CUT = 124
SWIFT = 125
HORN_ATTACK = 126
STOMP = 127
HEADBUTT = 128
HYPER_FANG = 129
SLAM = 130
BODY_SLAM = 131
REST = 132
STRUGGLE = 133
SCALD_BLASTOISE = 134
HYDRO_PUMP_BLASTOISE = 135
WRAP_GREEN = 136
WRAP_PINK = 137
FURY_CUTTER_FAST = 200
BUG_BITE_FAST = 201
BITE_FAST = 202
SUCKER_PUNCH_FAST = 203
DRAGON_BREATH_FAST = 204
THUNDER_SHOCK_FAST = 205
SPARK_FAST = 206
LOW_KICK_FAST = 207
KARATE_CHOP_FAST = 208
EMBER_FAST = 209
WING_ATTACK_FAST = 210
PECK_FAST = 211
LICK_FAST = 212
SHADOW_CLAW_FAST = 213
VINE_WHIP_FAST = 214
RAZOR_LEAF_FAST = 215
MUD_SHOT_FAST = 216
ICE_SHARD_FAST = 217
FROST_BREATH_FAST = 218
QUICK_ATTACK_FAST = 219
SCRATCH_FAST = 220
TACKLE_FAST = 221
POUND_FAST = 222
CUT_FAST = 223
POISON_JAB_FAST = 224
ACID_FAST = 225
PSYCHO_CUT_FAST = 226
ROCK_THROW_FAST = 227
METAL_CLAW_FAST = 228
BULLET_PUNCH_FAST = 229
WATER_GUN_FAST = 230
SPLASH_FAST = 231
WATER_GUN_FAST_BLASTOISE = 232
MUD_SLAP_FAST = 233
ZEN_HEADBUTT_FAST = 234
CONFUSION_FAST = 235
POISON_STING_FAST = 236
BUBBLE_FAST = 237
FEINT_ATTACK_FAST = 238
STEEL_WING_FAST = 239
FIRE_FANG_FAST = 240
ROCK_SMASH_FAST = 241


DESCRIPTOR.enum_types_by_name['PokemonMove'] = _POKEMONMOVE


# @@protoc_insertion_point(module_scope)
