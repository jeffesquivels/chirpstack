# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/api/multicast_group.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(chirpstack-api/api/multicast_group.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\"chirpstack-api/common/common.proto\"\xe0\x02\n\x0eMulticastGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x03 \x01(\t\x12\x1e\n\x06region\x18\x04 \x01(\x0e\x32\x0e.common.Region\x12\x0f\n\x07mc_addr\x18\x05 \x01(\t\x12\x14\n\x0cmc_nwk_s_key\x18\x06 \x01(\t\x12\x14\n\x0cmc_app_s_key\x18\x07 \x01(\t\x12\r\n\x05\x66_cnt\x18\x08 \x01(\r\x12+\n\ngroup_type\x18\t \x01(\x0e\x32\x17.api.MulticastGroupType\x12\n\n\x02\x64r\x18\n \x01(\r\x12\x11\n\tfrequency\x18\x0b \x01(\r\x12 \n\x18\x63lass_b_ping_slot_period\x18\x0c \x01(\r\x12\x42\n\x17\x63lass_c_scheduling_type\x18\r \x01(\x0e\x32!.api.MulticastGroupSchedulingType\"\xdf\x01\n\x16MulticastGroupListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x1e\n\x06region\x18\x05 \x01(\x0e\x32\x0e.common.Region\x12+\n\ngroup_type\x18\x06 \x01(\x0e\x32\x17.api.MulticastGroupType\"K\n\x1b\x43reateMulticastGroupRequest\x12,\n\x0fmulticast_group\x18\x01 \x01(\x0b\x32\x13.api.MulticastGroup\"*\n\x1c\x43reateMulticastGroupResponse\x12\n\n\x02id\x18\x01 \x01(\t\"&\n\x18GetMulticastGroupRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xa9\x01\n\x19GetMulticastGroupResponse\x12,\n\x0fmulticast_group\x18\x01 \x01(\x0b\x32\x13.api.MulticastGroup\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"K\n\x1bUpdateMulticastGroupRequest\x12,\n\x0fmulticast_group\x18\x01 \x01(\x0b\x32\x13.api.MulticastGroup\")\n\x1b\x44\x65leteMulticastGroupRequest\x12\n\n\x02id\x18\x01 \x01(\t\"c\n\x1aListMulticastGroupsRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0e\n\x06search\x18\x03 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x04 \x01(\t\"_\n\x1bListMulticastGroupsResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\r\x12+\n\x06result\x18\x02 \x03(\x0b\x32\x1b.api.MulticastGroupListItem\"O\n AddDeviceToMulticastGroupRequest\x12\x1a\n\x12multicast_group_id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65v_eui\x18\x02 \x01(\t\"T\n%RemoveDeviceFromMulticastGroupRequest\x12\x1a\n\x12multicast_group_id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65v_eui\x18\x02 \x01(\t\"S\n!AddGatewayToMulticastGroupRequest\x12\x1a\n\x12multicast_group_id\x18\x01 \x01(\t\x12\x12\n\ngateway_id\x18\x02 \x01(\t\"X\n&RemoveGatewayFromMulticastGroupRequest\x12\x1a\n\x12multicast_group_id\x18\x01 \x01(\t\x12\x12\n\ngateway_id\x18\x02 \x01(\t\"b\n\x17MulticastGroupQueueItem\x12\x1a\n\x12multicast_group_id\x18\x01 \x01(\t\x12\r\n\x05\x66_cnt\x18\x02 \x01(\r\x12\x0e\n\x06\x66_port\x18\x03 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"Y\n%EnqueueMulticastGroupQueueItemRequest\x12\x30\n\nqueue_item\x18\x01 \x01(\x0b\x32\x1c.api.MulticastGroupQueueItem\"7\n&EnqueueMulticastGroupQueueItemResponse\x12\r\n\x05\x66_cnt\x18\x01 \x01(\r\"=\n\x1f\x46lushMulticastGroupQueueRequest\x12\x1a\n\x12multicast_group_id\x18\x01 \x01(\t\"<\n\x1eListMulticastGroupQueueRequest\x12\x1a\n\x12multicast_group_id\x18\x01 \x01(\t\"N\n\x1fListMulticastGroupQueueResponse\x12+\n\x05items\x18\x01 \x03(\x0b\x32\x1c.api.MulticastGroupQueueItem*.\n\x12MulticastGroupType\x12\x0b\n\x07\x43LASS_C\x10\x00\x12\x0b\n\x07\x43LASS_B\x10\x01*7\n\x1cMulticastGroupSchedulingType\x12\t\n\x05\x44\x45LAY\x10\x00\x12\x0c\n\x08GPS_TIME\x10\x01\x32\xdd\x0c\n\x15MulticastGroupService\x12o\n\x06\x43reate\x12 .api.CreateMulticastGroupRequest\x1a!.api.CreateMulticastGroupResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/api/multicast-groups:\x01*\x12h\n\x03Get\x12\x1d.api.GetMulticastGroupRequest\x1a\x1e.api.GetMulticastGroupResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/multicast-groups/{id}\x12y\n\x06Update\x12 .api.UpdateMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"5\x82\xd3\xe4\x93\x02/\x1a*/api/multicast-groups/{multicast_group.id}:\x01*\x12\x66\n\x06\x44\x65lete\x12 .api.DeleteMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/api/multicast-groups/{id}\x12h\n\x04List\x12\x1f.api.ListMulticastGroupsRequest\x1a .api.ListMulticastGroupsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/api/multicast-groups\x12\x89\x01\n\tAddDevice\x12%.api.AddDeviceToMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"=\x82\xd3\xe4\x93\x02\x37\"2/api/multicast-groups/{multicast_group_id}/devices:\x01*\x12\x98\x01\n\x0cRemoveDevice\x12*.api.RemoveDeviceFromMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"D\x82\xd3\xe4\x93\x02>*</api/multicast-groups/{multicast_group_id}/devices/{dev_eui}\x12\x8c\x01\n\nAddGateway\x12&.api.AddGatewayToMulticastGroupRequest\x1a\x16.google.protobuf.Empty\">\x82\xd3\xe4\x93\x02\x38\"3/api/multicast-groups/{multicast_group_id}/gateways:\x01*\x12\x9e\x01\n\rRemoveGateway\x12+.api.RemoveGatewayFromMulticastGroupRequest\x1a\x16.google.protobuf.Empty\"H\x82\xd3\xe4\x93\x02\x42*@/api/multicast-groups/{multicast_group_id}/gateways/{gateway_id}\x12\xaa\x01\n\x07\x45nqueue\x12*.api.EnqueueMulticastGroupQueueItemRequest\x1a+.api.EnqueueMulticastGroupQueueItemResponse\"F\x82\xd3\xe4\x93\x02@\";/api/multicast-groups/{queue_item.multicast_group_id}/queue:\x01*\x12\x84\x01\n\nFlushQueue\x12$.api.FlushMulticastGroupQueueRequest\x1a\x16.google.protobuf.Empty\"8\x82\xd3\xe4\x93\x02\x32*0/api/multicast-groups/{multicast_group_id}/queue\x12\x90\x01\n\tListQueue\x12#.api.ListMulticastGroupQueueRequest\x1a$.api.ListMulticastGroupQueueResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/api/multicast-groups/{multicast_group_id}/queueBk\n\x11io.chirpstack.apiB\x13MulticastGroupProtoP\x01Z.github.com/chirpstack/chirpstack/api/go/v4/api\xaa\x02\x0e\x43hirpstack.Apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.api.multicast_group_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021io.chirpstack.apiB\023MulticastGroupProtoP\001Z.github.com/chirpstack/chirpstack/api/go/v4/api\252\002\016Chirpstack.Api'
  _MULTICASTGROUPSERVICE.methods_by_name['Create']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\032\"\025/api/multicast-groups:\001*'
  _MULTICASTGROUPSERVICE.methods_by_name['Get']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\034\022\032/api/multicast-groups/{id}'
  _MULTICASTGROUPSERVICE.methods_by_name['Update']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002/\032*/api/multicast-groups/{multicast_group.id}:\001*'
  _MULTICASTGROUPSERVICE.methods_by_name['Delete']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\034*\032/api/multicast-groups/{id}'
  _MULTICASTGROUPSERVICE.methods_by_name['List']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\027\022\025/api/multicast-groups'
  _MULTICASTGROUPSERVICE.methods_by_name['AddDevice']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['AddDevice']._serialized_options = b'\202\323\344\223\0027\"2/api/multicast-groups/{multicast_group_id}/devices:\001*'
  _MULTICASTGROUPSERVICE.methods_by_name['RemoveDevice']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['RemoveDevice']._serialized_options = b'\202\323\344\223\002>*</api/multicast-groups/{multicast_group_id}/devices/{dev_eui}'
  _MULTICASTGROUPSERVICE.methods_by_name['AddGateway']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['AddGateway']._serialized_options = b'\202\323\344\223\0028\"3/api/multicast-groups/{multicast_group_id}/gateways:\001*'
  _MULTICASTGROUPSERVICE.methods_by_name['RemoveGateway']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['RemoveGateway']._serialized_options = b'\202\323\344\223\002B*@/api/multicast-groups/{multicast_group_id}/gateways/{gateway_id}'
  _MULTICASTGROUPSERVICE.methods_by_name['Enqueue']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['Enqueue']._serialized_options = b'\202\323\344\223\002@\";/api/multicast-groups/{queue_item.multicast_group_id}/queue:\001*'
  _MULTICASTGROUPSERVICE.methods_by_name['FlushQueue']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['FlushQueue']._serialized_options = b'\202\323\344\223\0022*0/api/multicast-groups/{multicast_group_id}/queue'
  _MULTICASTGROUPSERVICE.methods_by_name['ListQueue']._options = None
  _MULTICASTGROUPSERVICE.methods_by_name['ListQueue']._serialized_options = b'\202\323\344\223\0022\0220/api/multicast-groups/{multicast_group_id}/queue'
  _MULTICASTGROUPTYPE._serialized_start=2204
  _MULTICASTGROUPTYPE._serialized_end=2250
  _MULTICASTGROUPSCHEDULINGTYPE._serialized_start=2252
  _MULTICASTGROUPSCHEDULINGTYPE._serialized_end=2307
  _MULTICASTGROUP._serialized_start=178
  _MULTICASTGROUP._serialized_end=530
  _MULTICASTGROUPLISTITEM._serialized_start=533
  _MULTICASTGROUPLISTITEM._serialized_end=756
  _CREATEMULTICASTGROUPREQUEST._serialized_start=758
  _CREATEMULTICASTGROUPREQUEST._serialized_end=833
  _CREATEMULTICASTGROUPRESPONSE._serialized_start=835
  _CREATEMULTICASTGROUPRESPONSE._serialized_end=877
  _GETMULTICASTGROUPREQUEST._serialized_start=879
  _GETMULTICASTGROUPREQUEST._serialized_end=917
  _GETMULTICASTGROUPRESPONSE._serialized_start=920
  _GETMULTICASTGROUPRESPONSE._serialized_end=1089
  _UPDATEMULTICASTGROUPREQUEST._serialized_start=1091
  _UPDATEMULTICASTGROUPREQUEST._serialized_end=1166
  _DELETEMULTICASTGROUPREQUEST._serialized_start=1168
  _DELETEMULTICASTGROUPREQUEST._serialized_end=1209
  _LISTMULTICASTGROUPSREQUEST._serialized_start=1211
  _LISTMULTICASTGROUPSREQUEST._serialized_end=1310
  _LISTMULTICASTGROUPSRESPONSE._serialized_start=1312
  _LISTMULTICASTGROUPSRESPONSE._serialized_end=1407
  _ADDDEVICETOMULTICASTGROUPREQUEST._serialized_start=1409
  _ADDDEVICETOMULTICASTGROUPREQUEST._serialized_end=1488
  _REMOVEDEVICEFROMMULTICASTGROUPREQUEST._serialized_start=1490
  _REMOVEDEVICEFROMMULTICASTGROUPREQUEST._serialized_end=1574
  _ADDGATEWAYTOMULTICASTGROUPREQUEST._serialized_start=1576
  _ADDGATEWAYTOMULTICASTGROUPREQUEST._serialized_end=1659
  _REMOVEGATEWAYFROMMULTICASTGROUPREQUEST._serialized_start=1661
  _REMOVEGATEWAYFROMMULTICASTGROUPREQUEST._serialized_end=1749
  _MULTICASTGROUPQUEUEITEM._serialized_start=1751
  _MULTICASTGROUPQUEUEITEM._serialized_end=1849
  _ENQUEUEMULTICASTGROUPQUEUEITEMREQUEST._serialized_start=1851
  _ENQUEUEMULTICASTGROUPQUEUEITEMREQUEST._serialized_end=1940
  _ENQUEUEMULTICASTGROUPQUEUEITEMRESPONSE._serialized_start=1942
  _ENQUEUEMULTICASTGROUPQUEUEITEMRESPONSE._serialized_end=1997
  _FLUSHMULTICASTGROUPQUEUEREQUEST._serialized_start=1999
  _FLUSHMULTICASTGROUPQUEUEREQUEST._serialized_end=2060
  _LISTMULTICASTGROUPQUEUEREQUEST._serialized_start=2062
  _LISTMULTICASTGROUPQUEUEREQUEST._serialized_end=2122
  _LISTMULTICASTGROUPQUEUERESPONSE._serialized_start=2124
  _LISTMULTICASTGROUPQUEUERESPONSE._serialized_end=2202
  _MULTICASTGROUPSERVICE._serialized_start=2310
  _MULTICASTGROUPSERVICE._serialized_end=3939
# @@protoc_insertion_point(module_scope)
