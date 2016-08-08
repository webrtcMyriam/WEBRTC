# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rtc_event_log.proto

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
  name='rtc_event_log.proto',
  package='webrtc.rtclog',
  syntax='proto2',
  serialized_pb=_b('\n\x13rtc_event_log.proto\x12\rwebrtc.rtclog\"3\n\x0b\x45ventStream\x12$\n\x06stream\x18\x01 \x03(\x0b\x32\x14.webrtc.rtclog.Event\"\xd4\x06\n\x05\x45vent\x12\x14\n\x0ctimestamp_us\x18\x01 \x01(\x03\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.webrtc.rtclog.Event.EventType\x12,\n\nrtp_packet\x18\x03 \x01(\x0b\x32\x18.webrtc.rtclog.RtpPacket\x12.\n\x0brtcp_packet\x18\x04 \x01(\x0b\x32\x19.webrtc.rtclog.RtcpPacket\x12=\n\x13\x61udio_playout_event\x18\x05 \x01(\x0b\x32 .webrtc.rtclog.AudioPlayoutEvent\x12@\n\x15\x62we_packet_loss_event\x18\x06 \x01(\x0b\x32!.webrtc.rtclog.BwePacketLossEvent\x12@\n\x15video_receiver_config\x18\x08 \x01(\x0b\x32!.webrtc.rtclog.VideoReceiveConfig\x12;\n\x13video_sender_config\x18\t \x01(\x0b\x32\x1e.webrtc.rtclog.VideoSendConfig\x12@\n\x15\x61udio_receiver_config\x18\n \x01(\x0b\x32!.webrtc.rtclog.AudioReceiveConfig\x12;\n\x13\x61udio_sender_config\x18\x0b \x01(\x0b\x32\x1e.webrtc.rtclog.AudioSendConfig\"\xa9\x02\n\tEventType\x12\x11\n\rUNKNOWN_EVENT\x10\x00\x12\r\n\tLOG_START\x10\x01\x12\x0b\n\x07LOG_END\x10\x02\x12\r\n\tRTP_EVENT\x10\x03\x12\x0e\n\nRTCP_EVENT\x10\x04\x12\x17\n\x13\x41UDIO_PLAYOUT_EVENT\x10\x05\x12\x19\n\x15\x42WE_PACKET_LOSS_EVENT\x10\x06\x12\x1a\n\x16\x42WE_PACKET_DELAY_EVENT\x10\x07\x12\x1f\n\x1bVIDEO_RECEIVER_CONFIG_EVENT\x10\x08\x12\x1d\n\x19VIDEO_SENDER_CONFIG_EVENT\x10\t\x12\x1f\n\x1b\x41UDIO_RECEIVER_CONFIG_EVENT\x10\n\x12\x1d\n\x19\x41UDIO_SENDER_CONFIG_EVENT\x10\x0b\"l\n\tRtpPacket\x12\x10\n\x08incoming\x18\x01 \x01(\x08\x12&\n\x04type\x18\x02 \x01(\x0e\x32\x18.webrtc.rtclog.MediaType\x12\x15\n\rpacket_length\x18\x03 \x01(\r\x12\x0e\n\x06header\x18\x04 \x01(\x0c\"[\n\nRtcpPacket\x12\x10\n\x08incoming\x18\x01 \x01(\x08\x12&\n\x04type\x18\x02 \x01(\x0e\x32\x18.webrtc.rtclog.MediaType\x12\x13\n\x0bpacket_data\x18\x03 \x01(\x0c\"\'\n\x11\x41udioPlayoutEvent\x12\x12\n\nlocal_ssrc\x18\x02 \x01(\r\"S\n\x12\x42wePacketLossEvent\x12\x0f\n\x07\x62itrate\x18\x01 \x01(\x05\x12\x15\n\rfraction_loss\x18\x02 \x01(\r\x12\x15\n\rtotal_packets\x18\x03 \x01(\x05\"\xd5\x02\n\x12VideoReceiveConfig\x12\x13\n\x0bremote_ssrc\x18\x01 \x01(\r\x12\x12\n\nlocal_ssrc\x18\x02 \x01(\r\x12=\n\trtcp_mode\x18\x03 \x01(\x0e\x32*.webrtc.rtclog.VideoReceiveConfig.RtcpMode\x12\x0c\n\x04remb\x18\x04 \x01(\x08\x12&\n\x07rtx_map\x18\x05 \x03(\x0b\x32\x15.webrtc.rtclog.RtxMap\x12<\n\x11header_extensions\x18\x06 \x03(\x0b\x32!.webrtc.rtclog.RtpHeaderExtension\x12.\n\x08\x64\x65\x63oders\x18\x07 \x03(\x0b\x32\x1c.webrtc.rtclog.DecoderConfig\"3\n\x08RtcpMode\x12\x11\n\rRTCP_COMPOUND\x10\x01\x12\x14\n\x10RTCP_REDUCEDSIZE\x10\x02\"3\n\rDecoderConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cpayload_type\x18\x02 \x01(\x05\".\n\x12RtpHeaderExtension\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\"7\n\tRtxConfig\x12\x10\n\x08rtx_ssrc\x18\x01 \x01(\r\x12\x18\n\x10rtx_payload_type\x18\x02 \x01(\x05\"H\n\x06RtxMap\x12\x14\n\x0cpayload_type\x18\x01 \x01(\x05\x12(\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x18.webrtc.rtclog.RtxConfig\"\xba\x01\n\x0fVideoSendConfig\x12\r\n\x05ssrcs\x18\x01 \x03(\r\x12<\n\x11header_extensions\x18\x02 \x03(\x0b\x32!.webrtc.rtclog.RtpHeaderExtension\x12\x11\n\trtx_ssrcs\x18\x03 \x03(\r\x12\x18\n\x10rtx_payload_type\x18\x04 \x01(\x05\x12-\n\x07\x65ncoder\x18\x05 \x01(\x0b\x32\x1c.webrtc.rtclog.EncoderConfig\"3\n\rEncoderConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cpayload_type\x18\x02 \x01(\x05\"{\n\x12\x41udioReceiveConfig\x12\x13\n\x0bremote_ssrc\x18\x01 \x01(\r\x12\x12\n\nlocal_ssrc\x18\x02 \x01(\r\x12<\n\x11header_extensions\x18\x03 \x03(\x0b\x32!.webrtc.rtclog.RtpHeaderExtension\"]\n\x0f\x41udioSendConfig\x12\x0c\n\x04ssrc\x18\x01 \x01(\r\x12<\n\x11header_extensions\x18\x02 \x03(\x0b\x32!.webrtc.rtclog.RtpHeaderExtension*4\n\tMediaType\x12\x07\n\x03\x41NY\x10\x00\x12\t\n\x05\x41UDIO\x10\x01\x12\t\n\x05VIDEO\x10\x02\x12\x08\n\x04\x44\x41TA\x10\x03\x42\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MEDIATYPE = _descriptor.EnumDescriptor(
  name='MediaType',
  full_name='webrtc.rtclog.MediaType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2313,
  serialized_end=2365,
)
_sym_db.RegisterEnumDescriptor(_MEDIATYPE)

MediaType = enum_type_wrapper.EnumTypeWrapper(_MEDIATYPE)
ANY = 0
AUDIO = 1
VIDEO = 2
DATA = 3


_EVENT_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='webrtc.rtclog.Event.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_EVENT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG_START', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG_END', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTP_EVENT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTCP_EVENT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO_PLAYOUT_EVENT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BWE_PACKET_LOSS_EVENT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BWE_PACKET_DELAY_EVENT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_RECEIVER_CONFIG_EVENT', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_SENDER_CONFIG_EVENT', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO_RECEIVER_CONFIG_EVENT', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO_SENDER_CONFIG_EVENT', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=647,
  serialized_end=944,
)
_sym_db.RegisterEnumDescriptor(_EVENT_EVENTTYPE)

_VIDEORECEIVECONFIG_RTCPMODE = _descriptor.EnumDescriptor(
  name='RtcpMode',
  full_name='webrtc.rtclog.VideoReceiveConfig.RtcpMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RTCP_COMPOUND', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTCP_REDUCEDSIZE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1566,
  serialized_end=1617,
)
_sym_db.RegisterEnumDescriptor(_VIDEORECEIVECONFIG_RTCPMODE)


_EVENTSTREAM = _descriptor.Descriptor(
  name='EventStream',
  full_name='webrtc.rtclog.EventStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream', full_name='webrtc.rtclog.EventStream.stream', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=38,
  serialized_end=89,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='webrtc.rtclog.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_us', full_name='webrtc.rtclog.Event.timestamp_us', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='webrtc.rtclog.Event.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtp_packet', full_name='webrtc.rtclog.Event.rtp_packet', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtcp_packet', full_name='webrtc.rtclog.Event.rtcp_packet', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_playout_event', full_name='webrtc.rtclog.Event.audio_playout_event', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bwe_packet_loss_event', full_name='webrtc.rtclog.Event.bwe_packet_loss_event', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_receiver_config', full_name='webrtc.rtclog.Event.video_receiver_config', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_sender_config', full_name='webrtc.rtclog.Event.video_sender_config', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_receiver_config', full_name='webrtc.rtclog.Event.audio_receiver_config', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audio_sender_config', full_name='webrtc.rtclog.Event.audio_sender_config', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVENT_EVENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=944,
)


_RTPPACKET = _descriptor.Descriptor(
  name='RtpPacket',
  full_name='webrtc.rtclog.RtpPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incoming', full_name='webrtc.rtclog.RtpPacket.incoming', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='webrtc.rtclog.RtpPacket.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packet_length', full_name='webrtc.rtclog.RtpPacket.packet_length', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='webrtc.rtclog.RtpPacket.header', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=946,
  serialized_end=1054,
)


_RTCPPACKET = _descriptor.Descriptor(
  name='RtcpPacket',
  full_name='webrtc.rtclog.RtcpPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incoming', full_name='webrtc.rtclog.RtcpPacket.incoming', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='webrtc.rtclog.RtcpPacket.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packet_data', full_name='webrtc.rtclog.RtcpPacket.packet_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1056,
  serialized_end=1147,
)


_AUDIOPLAYOUTEVENT = _descriptor.Descriptor(
  name='AudioPlayoutEvent',
  full_name='webrtc.rtclog.AudioPlayoutEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local_ssrc', full_name='webrtc.rtclog.AudioPlayoutEvent.local_ssrc', index=0,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=1149,
  serialized_end=1188,
)


_BWEPACKETLOSSEVENT = _descriptor.Descriptor(
  name='BwePacketLossEvent',
  full_name='webrtc.rtclog.BwePacketLossEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bitrate', full_name='webrtc.rtclog.BwePacketLossEvent.bitrate', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fraction_loss', full_name='webrtc.rtclog.BwePacketLossEvent.fraction_loss', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_packets', full_name='webrtc.rtclog.BwePacketLossEvent.total_packets', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=1190,
  serialized_end=1273,
)


_VIDEORECEIVECONFIG = _descriptor.Descriptor(
  name='VideoReceiveConfig',
  full_name='webrtc.rtclog.VideoReceiveConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remote_ssrc', full_name='webrtc.rtclog.VideoReceiveConfig.remote_ssrc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_ssrc', full_name='webrtc.rtclog.VideoReceiveConfig.local_ssrc', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtcp_mode', full_name='webrtc.rtclog.VideoReceiveConfig.rtcp_mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remb', full_name='webrtc.rtclog.VideoReceiveConfig.remb', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtx_map', full_name='webrtc.rtclog.VideoReceiveConfig.rtx_map', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_extensions', full_name='webrtc.rtclog.VideoReceiveConfig.header_extensions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decoders', full_name='webrtc.rtclog.VideoReceiveConfig.decoders', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VIDEORECEIVECONFIG_RTCPMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1276,
  serialized_end=1617,
)


_DECODERCONFIG = _descriptor.Descriptor(
  name='DecoderConfig',
  full_name='webrtc.rtclog.DecoderConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='webrtc.rtclog.DecoderConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_type', full_name='webrtc.rtclog.DecoderConfig.payload_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=1619,
  serialized_end=1670,
)


_RTPHEADEREXTENSION = _descriptor.Descriptor(
  name='RtpHeaderExtension',
  full_name='webrtc.rtclog.RtpHeaderExtension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='webrtc.rtclog.RtpHeaderExtension.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='webrtc.rtclog.RtpHeaderExtension.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=1672,
  serialized_end=1718,
)


_RTXCONFIG = _descriptor.Descriptor(
  name='RtxConfig',
  full_name='webrtc.rtclog.RtxConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rtx_ssrc', full_name='webrtc.rtclog.RtxConfig.rtx_ssrc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtx_payload_type', full_name='webrtc.rtclog.RtxConfig.rtx_payload_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=1720,
  serialized_end=1775,
)


_RTXMAP = _descriptor.Descriptor(
  name='RtxMap',
  full_name='webrtc.rtclog.RtxMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload_type', full_name='webrtc.rtclog.RtxMap.payload_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config', full_name='webrtc.rtclog.RtxMap.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1777,
  serialized_end=1849,
)


_VIDEOSENDCONFIG = _descriptor.Descriptor(
  name='VideoSendConfig',
  full_name='webrtc.rtclog.VideoSendConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssrcs', full_name='webrtc.rtclog.VideoSendConfig.ssrcs', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_extensions', full_name='webrtc.rtclog.VideoSendConfig.header_extensions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtx_ssrcs', full_name='webrtc.rtclog.VideoSendConfig.rtx_ssrcs', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtx_payload_type', full_name='webrtc.rtclog.VideoSendConfig.rtx_payload_type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encoder', full_name='webrtc.rtclog.VideoSendConfig.encoder', index=4,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1852,
  serialized_end=2038,
)


_ENCODERCONFIG = _descriptor.Descriptor(
  name='EncoderConfig',
  full_name='webrtc.rtclog.EncoderConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='webrtc.rtclog.EncoderConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_type', full_name='webrtc.rtclog.EncoderConfig.payload_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=2040,
  serialized_end=2091,
)


_AUDIORECEIVECONFIG = _descriptor.Descriptor(
  name='AudioReceiveConfig',
  full_name='webrtc.rtclog.AudioReceiveConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remote_ssrc', full_name='webrtc.rtclog.AudioReceiveConfig.remote_ssrc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_ssrc', full_name='webrtc.rtclog.AudioReceiveConfig.local_ssrc', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_extensions', full_name='webrtc.rtclog.AudioReceiveConfig.header_extensions', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=2093,
  serialized_end=2216,
)


_AUDIOSENDCONFIG = _descriptor.Descriptor(
  name='AudioSendConfig',
  full_name='webrtc.rtclog.AudioSendConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssrc', full_name='webrtc.rtclog.AudioSendConfig.ssrc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_extensions', full_name='webrtc.rtclog.AudioSendConfig.header_extensions', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=2218,
  serialized_end=2311,
)

_EVENTSTREAM.fields_by_name['stream'].message_type = _EVENT
_EVENT.fields_by_name['type'].enum_type = _EVENT_EVENTTYPE
_EVENT.fields_by_name['rtp_packet'].message_type = _RTPPACKET
_EVENT.fields_by_name['rtcp_packet'].message_type = _RTCPPACKET
_EVENT.fields_by_name['audio_playout_event'].message_type = _AUDIOPLAYOUTEVENT
_EVENT.fields_by_name['bwe_packet_loss_event'].message_type = _BWEPACKETLOSSEVENT
_EVENT.fields_by_name['video_receiver_config'].message_type = _VIDEORECEIVECONFIG
_EVENT.fields_by_name['video_sender_config'].message_type = _VIDEOSENDCONFIG
_EVENT.fields_by_name['audio_receiver_config'].message_type = _AUDIORECEIVECONFIG
_EVENT.fields_by_name['audio_sender_config'].message_type = _AUDIOSENDCONFIG
_EVENT_EVENTTYPE.containing_type = _EVENT
_RTPPACKET.fields_by_name['type'].enum_type = _MEDIATYPE
_RTCPPACKET.fields_by_name['type'].enum_type = _MEDIATYPE
_VIDEORECEIVECONFIG.fields_by_name['rtcp_mode'].enum_type = _VIDEORECEIVECONFIG_RTCPMODE
_VIDEORECEIVECONFIG.fields_by_name['rtx_map'].message_type = _RTXMAP
_VIDEORECEIVECONFIG.fields_by_name['header_extensions'].message_type = _RTPHEADEREXTENSION
_VIDEORECEIVECONFIG.fields_by_name['decoders'].message_type = _DECODERCONFIG
_VIDEORECEIVECONFIG_RTCPMODE.containing_type = _VIDEORECEIVECONFIG
_RTXMAP.fields_by_name['config'].message_type = _RTXCONFIG
_VIDEOSENDCONFIG.fields_by_name['header_extensions'].message_type = _RTPHEADEREXTENSION
_VIDEOSENDCONFIG.fields_by_name['encoder'].message_type = _ENCODERCONFIG
_AUDIORECEIVECONFIG.fields_by_name['header_extensions'].message_type = _RTPHEADEREXTENSION
_AUDIOSENDCONFIG.fields_by_name['header_extensions'].message_type = _RTPHEADEREXTENSION
DESCRIPTOR.message_types_by_name['EventStream'] = _EVENTSTREAM
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['RtpPacket'] = _RTPPACKET
DESCRIPTOR.message_types_by_name['RtcpPacket'] = _RTCPPACKET
DESCRIPTOR.message_types_by_name['AudioPlayoutEvent'] = _AUDIOPLAYOUTEVENT
DESCRIPTOR.message_types_by_name['BwePacketLossEvent'] = _BWEPACKETLOSSEVENT
DESCRIPTOR.message_types_by_name['VideoReceiveConfig'] = _VIDEORECEIVECONFIG
DESCRIPTOR.message_types_by_name['DecoderConfig'] = _DECODERCONFIG
DESCRIPTOR.message_types_by_name['RtpHeaderExtension'] = _RTPHEADEREXTENSION
DESCRIPTOR.message_types_by_name['RtxConfig'] = _RTXCONFIG
DESCRIPTOR.message_types_by_name['RtxMap'] = _RTXMAP
DESCRIPTOR.message_types_by_name['VideoSendConfig'] = _VIDEOSENDCONFIG
DESCRIPTOR.message_types_by_name['EncoderConfig'] = _ENCODERCONFIG
DESCRIPTOR.message_types_by_name['AudioReceiveConfig'] = _AUDIORECEIVECONFIG
DESCRIPTOR.message_types_by_name['AudioSendConfig'] = _AUDIOSENDCONFIG
DESCRIPTOR.enum_types_by_name['MediaType'] = _MEDIATYPE

EventStream = _reflection.GeneratedProtocolMessageType('EventStream', (_message.Message,), dict(
  DESCRIPTOR = _EVENTSTREAM,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.EventStream)
  ))
_sym_db.RegisterMessage(EventStream)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.Event)
  ))
_sym_db.RegisterMessage(Event)

RtpPacket = _reflection.GeneratedProtocolMessageType('RtpPacket', (_message.Message,), dict(
  DESCRIPTOR = _RTPPACKET,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.RtpPacket)
  ))
_sym_db.RegisterMessage(RtpPacket)

RtcpPacket = _reflection.GeneratedProtocolMessageType('RtcpPacket', (_message.Message,), dict(
  DESCRIPTOR = _RTCPPACKET,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.RtcpPacket)
  ))
_sym_db.RegisterMessage(RtcpPacket)

AudioPlayoutEvent = _reflection.GeneratedProtocolMessageType('AudioPlayoutEvent', (_message.Message,), dict(
  DESCRIPTOR = _AUDIOPLAYOUTEVENT,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.AudioPlayoutEvent)
  ))
_sym_db.RegisterMessage(AudioPlayoutEvent)

BwePacketLossEvent = _reflection.GeneratedProtocolMessageType('BwePacketLossEvent', (_message.Message,), dict(
  DESCRIPTOR = _BWEPACKETLOSSEVENT,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.BwePacketLossEvent)
  ))
_sym_db.RegisterMessage(BwePacketLossEvent)

VideoReceiveConfig = _reflection.GeneratedProtocolMessageType('VideoReceiveConfig', (_message.Message,), dict(
  DESCRIPTOR = _VIDEORECEIVECONFIG,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.VideoReceiveConfig)
  ))
_sym_db.RegisterMessage(VideoReceiveConfig)

DecoderConfig = _reflection.GeneratedProtocolMessageType('DecoderConfig', (_message.Message,), dict(
  DESCRIPTOR = _DECODERCONFIG,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.DecoderConfig)
  ))
_sym_db.RegisterMessage(DecoderConfig)

RtpHeaderExtension = _reflection.GeneratedProtocolMessageType('RtpHeaderExtension', (_message.Message,), dict(
  DESCRIPTOR = _RTPHEADEREXTENSION,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.RtpHeaderExtension)
  ))
_sym_db.RegisterMessage(RtpHeaderExtension)

RtxConfig = _reflection.GeneratedProtocolMessageType('RtxConfig', (_message.Message,), dict(
  DESCRIPTOR = _RTXCONFIG,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.RtxConfig)
  ))
_sym_db.RegisterMessage(RtxConfig)

RtxMap = _reflection.GeneratedProtocolMessageType('RtxMap', (_message.Message,), dict(
  DESCRIPTOR = _RTXMAP,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.RtxMap)
  ))
_sym_db.RegisterMessage(RtxMap)

VideoSendConfig = _reflection.GeneratedProtocolMessageType('VideoSendConfig', (_message.Message,), dict(
  DESCRIPTOR = _VIDEOSENDCONFIG,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.VideoSendConfig)
  ))
_sym_db.RegisterMessage(VideoSendConfig)

EncoderConfig = _reflection.GeneratedProtocolMessageType('EncoderConfig', (_message.Message,), dict(
  DESCRIPTOR = _ENCODERCONFIG,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.EncoderConfig)
  ))
_sym_db.RegisterMessage(EncoderConfig)

AudioReceiveConfig = _reflection.GeneratedProtocolMessageType('AudioReceiveConfig', (_message.Message,), dict(
  DESCRIPTOR = _AUDIORECEIVECONFIG,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.AudioReceiveConfig)
  ))
_sym_db.RegisterMessage(AudioReceiveConfig)

AudioSendConfig = _reflection.GeneratedProtocolMessageType('AudioSendConfig', (_message.Message,), dict(
  DESCRIPTOR = _AUDIOSENDCONFIG,
  __module__ = 'rtc_event_log_pb2'
  # @@protoc_insertion_point(class_scope:webrtc.rtclog.AudioSendConfig)
  ))
_sym_db.RegisterMessage(AudioSendConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
