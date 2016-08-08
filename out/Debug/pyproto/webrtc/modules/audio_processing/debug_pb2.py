# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: debug.proto

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
  name='debug.proto',
  package='webrtc.audioproc',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x64\x65\x62ug.proto\x12\x10webrtc.audioproc\"\x94\x02\n\x04Init\x12\x13\n\x0bsample_rate\x18\x01 \x01(\x05\x12\x1e\n\x12\x64\x65vice_sample_rate\x18\x02 \x01(\x05\x42\x02\x18\x01\x12\x1a\n\x12num_input_channels\x18\x03 \x01(\x05\x12\x1b\n\x13num_output_channels\x18\x04 \x01(\x05\x12\x1c\n\x14num_reverse_channels\x18\x05 \x01(\x05\x12\x1b\n\x13reverse_sample_rate\x18\x06 \x01(\x05\x12\x1a\n\x12output_sample_rate\x18\x07 \x01(\x05\x12\"\n\x1areverse_output_sample_rate\x18\x08 \x01(\x05\x12#\n\x1bnum_reverse_output_channels\x18\t \x01(\x05\".\n\rReverseStream\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0f\n\x07\x63hannel\x18\x02 \x03(\x0c\"\x9f\x01\n\x06Stream\x12\x12\n\ninput_data\x18\x01 \x01(\x0c\x12\x13\n\x0boutput_data\x18\x02 \x01(\x0c\x12\r\n\x05\x64\x65lay\x18\x03 \x01(\x05\x12\r\n\x05\x64rift\x18\x04 \x01(\x11\x12\r\n\x05level\x18\x05 \x01(\x05\x12\x10\n\x08keypress\x18\x06 \x01(\x08\x12\x15\n\rinput_channel\x18\x07 \x03(\x0c\x12\x16\n\x0eoutput_channel\x18\x08 \x03(\x0c\"\x95\x04\n\x06\x43onfig\x12\x13\n\x0b\x61\x65\x63_enabled\x18\x01 \x01(\x08\x12\"\n\x1a\x61\x65\x63_delay_agnostic_enabled\x18\x02 \x01(\x08\x12&\n\x1e\x61\x65\x63_drift_compensation_enabled\x18\x03 \x01(\x08\x12#\n\x1b\x61\x65\x63_extended_filter_enabled\x18\x04 \x01(\x08\x12\x1d\n\x15\x61\x65\x63_suppression_level\x18\x05 \x01(\x05\x12\x14\n\x0c\x61\x65\x63m_enabled\x18\x06 \x01(\x08\x12\"\n\x1a\x61\x65\x63m_comfort_noise_enabled\x18\x07 \x01(\x08\x12\x19\n\x11\x61\x65\x63m_routing_mode\x18\x08 \x01(\x05\x12\x13\n\x0b\x61gc_enabled\x18\t \x01(\x08\x12\x10\n\x08\x61gc_mode\x18\n \x01(\x05\x12\x1b\n\x13\x61gc_limiter_enabled\x18\x0b \x01(\x08\x12 \n\x18noise_robust_agc_enabled\x18\x0c \x01(\x08\x12\x13\n\x0bhpf_enabled\x18\r \x01(\x08\x12\x12\n\nns_enabled\x18\x0e \x01(\x08\x12\x10\n\x08ns_level\x18\x0f \x01(\x05\x12%\n\x1dtransient_suppression_enabled\x18\x10 \x01(\x08\x12\x1f\n\x17\x65xperiments_description\x18\x11 \x01(\t\x12(\n intelligibility_enhancer_enabled\x18\x12 \x01(\x08\"\xb7\x02\n\x05\x45vent\x12*\n\x04type\x18\x01 \x02(\x0e\x32\x1c.webrtc.audioproc.Event.Type\x12$\n\x04init\x18\x02 \x01(\x0b\x32\x16.webrtc.audioproc.Init\x12\x37\n\x0ereverse_stream\x18\x03 \x01(\x0b\x32\x1f.webrtc.audioproc.ReverseStream\x12(\n\x06stream\x18\x04 \x01(\x0b\x32\x18.webrtc.audioproc.Stream\x12(\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x18.webrtc.audioproc.Config\"O\n\x04Type\x12\x08\n\x04INIT\x10\x00\x12\x12\n\x0eREVERSE_STREAM\x10\x01\x12\n\n\x06STREAM\x10\x02\x12\n\n\x06\x43ONFIG\x10\x03\x12\x11\n\rUNKNOWN_EVENT\x10\x04\x42\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_EVENT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='webrtc.audioproc.Event.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVERSE_STREAM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STREAM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIG', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_EVENT', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1291,
  serialized_end=1370,
)
_sym_db.RegisterEnumDescriptor(_EVENT_TYPE)


_INIT = _descriptor.Descriptor(
  name='Init',
  full_name='webrtc.audioproc.Init',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate', full_name='webrtc.audioproc.Init.sample_rate', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_sample_rate', full_name='webrtc.audioproc.Init.device_sample_rate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='num_input_channels', full_name='webrtc.audioproc.Init.num_input_channels', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_output_channels', full_name='webrtc.audioproc.Init.num_output_channels', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_reverse_channels', full_name='webrtc.audioproc.Init.num_reverse_channels', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse_sample_rate', full_name='webrtc.audioproc.Init.reverse_sample_rate', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_sample_rate', full_name='webrtc.audioproc.Init.output_sample_rate', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse_output_sample_rate', full_name='webrtc.audioproc.Init.reverse_output_sample_rate', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_reverse_output_channels', full_name='webrtc.audioproc.Init.num_reverse_output_channels', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=310,
)


_REVERSESTREAM = _descriptor.Descriptor(
  name='ReverseStream',
  full_name='webrtc.audioproc.ReverseStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='webrtc.audioproc.ReverseStream.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='webrtc.audioproc.ReverseStream.channel', index=1,
      number=2, type=12, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=358,
)


_STREAM = _descriptor.Descriptor(
  name='Stream',
  full_name='webrtc.audioproc.Stream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_data', full_name='webrtc.audioproc.Stream.input_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_data', full_name='webrtc.audioproc.Stream.output_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delay', full_name='webrtc.audioproc.Stream.delay', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drift', full_name='webrtc.audioproc.Stream.drift', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='webrtc.audioproc.Stream.level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypress', full_name='webrtc.audioproc.Stream.keypress', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_channel', full_name='webrtc.audioproc.Stream.input_channel', index=6,
      number=7, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_channel', full_name='webrtc.audioproc.Stream.output_channel', index=7,
      number=8, type=12, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=520,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='webrtc.audioproc.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aec_enabled', full_name='webrtc.audioproc.Config.aec_enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aec_delay_agnostic_enabled', full_name='webrtc.audioproc.Config.aec_delay_agnostic_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aec_drift_compensation_enabled', full_name='webrtc.audioproc.Config.aec_drift_compensation_enabled', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aec_extended_filter_enabled', full_name='webrtc.audioproc.Config.aec_extended_filter_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aec_suppression_level', full_name='webrtc.audioproc.Config.aec_suppression_level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aecm_enabled', full_name='webrtc.audioproc.Config.aecm_enabled', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aecm_comfort_noise_enabled', full_name='webrtc.audioproc.Config.aecm_comfort_noise_enabled', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aecm_routing_mode', full_name='webrtc.audioproc.Config.aecm_routing_mode', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agc_enabled', full_name='webrtc.audioproc.Config.agc_enabled', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agc_mode', full_name='webrtc.audioproc.Config.agc_mode', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agc_limiter_enabled', full_name='webrtc.audioproc.Config.agc_limiter_enabled', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='noise_robust_agc_enabled', full_name='webrtc.audioproc.Config.noise_robust_agc_enabled', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hpf_enabled', full_name='webrtc.audioproc.Config.hpf_enabled', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ns_enabled', full_name='webrtc.audioproc.Config.ns_enabled', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ns_level', full_name='webrtc.audioproc.Config.ns_level', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transient_suppression_enabled', full_name='webrtc.audioproc.Config.transient_suppression_enabled', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experiments_description', full_name='webrtc.audioproc.Config.experiments_description', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intelligibility_enhancer_enabled', full_name='webrtc.audioproc.Config.intelligibility_enhancer_enabled', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=523,
  serialized_end=1056,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='webrtc.audioproc.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='webrtc.audioproc.Event.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init', full_name='webrtc.audioproc.Event.init', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse_stream', full_name='webrtc.audioproc.Event.reverse_stream', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream', full_name='webrtc.audioproc.Event.stream', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config', full_name='webrtc.audioproc.Event.config', index=4,
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
    _EVENT_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1059,
  serialized_end=1370,
)

_EVENT.fields_by_name['type'].enum_type = _EVENT_TYPE
_EVENT.fields_by_name['init'].message_type = _INIT
_EVENT.fields_by_name['reverse_stream'].message_type = _REVERSESTREAM
_EVENT.fields_by_name['stream'].message_type = _STREAM
_EVENT.fields_by_name['config'].message_type = _CONFIG
_EVENT_TYPE.containing_type = _EVENT
DESCRIPTOR.message_types_by_name['Init'] = _INIT
DESCRIPTOR.message_types_by_name['ReverseStream'] = _REVERSESTREAM
DESCRIPTOR.message_types_by_name['Stream'] = _STREAM
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Event'] = _EVENT

Init = _reflection.GeneratedProtocolMessageType('Init', (_message.Message,), dict(
  DESCRIPTOR = _INIT,
  __module__ = 'debug_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.audioproc.Init)
  ))
_sym_db.RegisterMessage(Init)

ReverseStream = _reflection.GeneratedProtocolMessageType('ReverseStream', (_message.Message,), dict(
  DESCRIPTOR = _REVERSESTREAM,
  __module__ = 'debug_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.audioproc.ReverseStream)
  ))
_sym_db.RegisterMessage(ReverseStream)

Stream = _reflection.GeneratedProtocolMessageType('Stream', (_message.Message,), dict(
  DESCRIPTOR = _STREAM,
  __module__ = 'debug_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.audioproc.Stream)
  ))
_sym_db.RegisterMessage(Stream)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'debug_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.audioproc.Config)
  ))
_sym_db.RegisterMessage(Config)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'debug_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.audioproc.Event)
  ))
_sym_db.RegisterMessage(Event)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
_INIT.fields_by_name['device_sample_rate'].has_options = True
_INIT.fields_by_name['device_sample_rate']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)
