# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: neteq_unittest.proto

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
  name='neteq_unittest.proto',
  package='webrtc.neteq_unittest',
  syntax='proto2',
  serialized_pb=_b('\n\x14neteq_unittest.proto\x12\x15webrtc.neteq_unittest\"\xdc\x03\n\x16NetEqNetworkStatistics\x12\x1e\n\x16\x63urrent_buffer_size_ms\x18\x01 \x01(\r\x12 \n\x18preferred_buffer_size_ms\x18\x02 \x01(\r\x12\x1a\n\x12jitter_peaks_found\x18\x03 \x01(\r\x12\x18\n\x10packet_loss_rate\x18\x04 \x01(\r\x12\x1b\n\x13packet_discard_rate\x18\x05 \x01(\r\x12\x13\n\x0b\x65xpand_rate\x18\x06 \x01(\r\x12\x1a\n\x12speech_expand_rate\x18\x07 \x01(\r\x12\x17\n\x0fpreemptive_rate\x18\x08 \x01(\r\x12\x17\n\x0f\x61\x63\x63\x65lerate_rate\x18\t \x01(\r\x12\x1e\n\x16secondary_decoded_rate\x18\n \x01(\r\x12\x16\n\x0e\x63lockdrift_ppm\x18\x0b \x01(\x05\x12\x1a\n\x12\x61\x64\x64\x65\x64_zero_samples\x18\x0c \x01(\x04\x12\x1c\n\x14mean_waiting_time_ms\x18\r \x01(\x05\x12\x1e\n\x16median_waiting_time_ms\x18\x0e \x01(\x05\x12\x1b\n\x13min_waiting_time_ms\x18\x0f \x01(\x05\x12\x1b\n\x13max_waiting_time_ms\x18\x10 \x01(\x05\"v\n\x0eRtcpStatistics\x12\x15\n\rfraction_lost\x18\x01 \x01(\r\x12\x17\n\x0f\x63umulative_lost\x18\x02 \x01(\r\x12$\n\x1c\x65xtended_max_sequence_number\x18\x03 \x01(\r\x12\x0e\n\x06jitter\x18\x04 \x01(\rB\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_NETEQNETWORKSTATISTICS = _descriptor.Descriptor(
  name='NetEqNetworkStatistics',
  full_name='webrtc.neteq_unittest.NetEqNetworkStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_buffer_size_ms', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.current_buffer_size_ms', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preferred_buffer_size_ms', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.preferred_buffer_size_ms', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jitter_peaks_found', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.jitter_peaks_found', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packet_loss_rate', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.packet_loss_rate', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packet_discard_rate', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.packet_discard_rate', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expand_rate', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.expand_rate', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speech_expand_rate', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.speech_expand_rate', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preemptive_rate', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.preemptive_rate', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accelerate_rate', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.accelerate_rate', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secondary_decoded_rate', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.secondary_decoded_rate', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clockdrift_ppm', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.clockdrift_ppm', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='added_zero_samples', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.added_zero_samples', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mean_waiting_time_ms', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.mean_waiting_time_ms', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='median_waiting_time_ms', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.median_waiting_time_ms', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_waiting_time_ms', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.min_waiting_time_ms', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_waiting_time_ms', full_name='webrtc.neteq_unittest.NetEqNetworkStatistics.max_waiting_time_ms', index=15,
      number=16, type=5, cpp_type=1, label=1,
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
  serialized_start=48,
  serialized_end=524,
)


_RTCPSTATISTICS = _descriptor.Descriptor(
  name='RtcpStatistics',
  full_name='webrtc.neteq_unittest.RtcpStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fraction_lost', full_name='webrtc.neteq_unittest.RtcpStatistics.fraction_lost', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cumulative_lost', full_name='webrtc.neteq_unittest.RtcpStatistics.cumulative_lost', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extended_max_sequence_number', full_name='webrtc.neteq_unittest.RtcpStatistics.extended_max_sequence_number', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jitter', full_name='webrtc.neteq_unittest.RtcpStatistics.jitter', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=526,
  serialized_end=644,
)

DESCRIPTOR.message_types_by_name['NetEqNetworkStatistics'] = _NETEQNETWORKSTATISTICS
DESCRIPTOR.message_types_by_name['RtcpStatistics'] = _RTCPSTATISTICS

NetEqNetworkStatistics = _reflection.GeneratedProtocolMessageType('NetEqNetworkStatistics', (_message.Message,), dict(
  DESCRIPTOR = _NETEQNETWORKSTATISTICS,
  __module__ = 'neteq_unittest_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.neteq_unittest.NetEqNetworkStatistics)
  ))
_sym_db.RegisterMessage(NetEqNetworkStatistics)

RtcpStatistics = _reflection.GeneratedProtocolMessageType('RtcpStatistics', (_message.Message,), dict(
  DESCRIPTOR = _RTCPSTATISTICS,
  __module__ = 'neteq_unittest_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.neteq_unittest.RtcpStatistics)
  ))
_sym_db.RegisterMessage(RtcpStatistics)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
