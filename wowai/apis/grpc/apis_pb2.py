# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apis/grpc/apis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pis/grpc/apis.proto\x12\nwowai.apis\x1a\x1bgoogle/protobuf/empty.proto\".\n\x0b\x41uthRequest\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"-\n\x0c\x41uthResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"&\n\x18\x43ustomUserDestroyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x17\n\x15\x43ustomUserListRequest\"I\n\x16\x43ustomUserListResponse\x12/\n\x07results\x18\x01 \x03(\x0b\x32\x1e.wowai.apis.CustomUserResponse\"n\n\x1e\x43ustomUserPartialUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x11\n\tis_active\x18\x03 \x01(\x08\x12\x1e\n\x16_partial_update_fields\x18\x04 \x03(\t\"A\n\x11\x43ustomUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x11\n\tis_active\x18\x03 \x01(\x08\"B\n\x12\x43ustomUserResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x11\n\tis_active\x18\x04 \x01(\x08\"\'\n\x19\x43ustomUserRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32Q\n\x10\x41uthenController\x12=\n\x06\x43reate\x12\x17.wowai.apis.AuthRequest\x1a\x18.wowai.apis.AuthResponse\"\x00\x32\xfc\x03\n\x14\x43ustomUserController\x12I\n\x06\x43reate\x12\x1d.wowai.apis.CustomUserRequest\x1a\x1e.wowai.apis.CustomUserResponse\"\x00\x12I\n\x07\x44\x65stroy\x12$.wowai.apis.CustomUserDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12O\n\x04List\x12!.wowai.apis.CustomUserListRequest\x1a\".wowai.apis.CustomUserListResponse\"\x00\x12]\n\rPartialUpdate\x12*.wowai.apis.CustomUserPartialUpdateRequest\x1a\x1e.wowai.apis.CustomUserResponse\"\x00\x12S\n\x08Retrieve\x12%.wowai.apis.CustomUserRetrieveRequest\x1a\x1e.wowai.apis.CustomUserResponse\"\x00\x12I\n\x06Update\x12\x1d.wowai.apis.CustomUserRequest\x1a\x1e.wowai.apis.CustomUserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apis.grpc.apis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_AUTHREQUEST']._serialized_start=65
  _globals['_AUTHREQUEST']._serialized_end=111
  _globals['_AUTHRESPONSE']._serialized_start=113
  _globals['_AUTHRESPONSE']._serialized_end=158
  _globals['_CUSTOMUSERDESTROYREQUEST']._serialized_start=160
  _globals['_CUSTOMUSERDESTROYREQUEST']._serialized_end=198
  _globals['_CUSTOMUSERLISTREQUEST']._serialized_start=200
  _globals['_CUSTOMUSERLISTREQUEST']._serialized_end=223
  _globals['_CUSTOMUSERLISTRESPONSE']._serialized_start=225
  _globals['_CUSTOMUSERLISTRESPONSE']._serialized_end=298
  _globals['_CUSTOMUSERPARTIALUPDATEREQUEST']._serialized_start=300
  _globals['_CUSTOMUSERPARTIALUPDATEREQUEST']._serialized_end=410
  _globals['_CUSTOMUSERREQUEST']._serialized_start=412
  _globals['_CUSTOMUSERREQUEST']._serialized_end=477
  _globals['_CUSTOMUSERRESPONSE']._serialized_start=479
  _globals['_CUSTOMUSERRESPONSE']._serialized_end=545
  _globals['_CUSTOMUSERRETRIEVEREQUEST']._serialized_start=547
  _globals['_CUSTOMUSERRETRIEVEREQUEST']._serialized_end=586
  _globals['_AUTHENCONTROLLER']._serialized_start=588
  _globals['_AUTHENCONTROLLER']._serialized_end=669
  _globals['_CUSTOMUSERCONTROLLER']._serialized_start=672
  _globals['_CUSTOMUSERCONTROLLER']._serialized_end=1180
# @@protoc_insertion_point(module_scope)