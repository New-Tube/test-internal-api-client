# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\x12\x0cinternal_api\"2\n\x0eStatusResponse\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x0f\n\x07Message\x18\x02 \x01(\t\"-\n\x0fReactionRequest\x12\x0e\n\x06UserID\x18\x01 \x01(\x04\x12\n\n\x02ID\x18\x02 \x01(\x04\"5\n\x10ReactionResponse\x12\x0e\n\x06IsLike\x18\x01 \x01(\x08\x12\x11\n\tIsDislike\x18\x02 \x01(\x08\"V\n\x15UpdateReactionRequest\x12\n\n\x02ID\x18\x01 \x01(\x04\x12\x0e\n\x06UserID\x18\x02 \x01(\x04\x12\x0e\n\x06IsLike\x18\x03 \x01(\x08\x12\x11\n\tIsDislike\x18\x04 \x01(\x08\x42)Z\'github.com/New-Tube/internal-api-protosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/New-Tube/internal-api-protos'
  _globals['_STATUSRESPONSE']._serialized_start=30
  _globals['_STATUSRESPONSE']._serialized_end=80
  _globals['_REACTIONREQUEST']._serialized_start=82
  _globals['_REACTIONREQUEST']._serialized_end=127
  _globals['_REACTIONRESPONSE']._serialized_start=129
  _globals['_REACTIONRESPONSE']._serialized_end=182
  _globals['_UPDATEREACTIONREQUEST']._serialized_start=184
  _globals['_UPDATEREACTIONREQUEST']._serialized_end=270
# @@protoc_insertion_point(module_scope)
