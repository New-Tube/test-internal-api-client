from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Privacy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Public: _ClassVar[Privacy]
    Link: _ClassVar[Privacy]
    Private: _ClassVar[Privacy]
Public: Privacy
Link: Privacy
Private: Privacy

class VideoRequest(_message.Message):
    __slots__ = ("ID", "UserID")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    ID: int
    UserID: int
    def __init__(self, ID: _Optional[int] = ..., UserID: _Optional[int] = ...) -> None: ...
