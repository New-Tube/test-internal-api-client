import video_pb2 as _video_pb2
import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoCreateResponse(_message.Message):
    __slots__ = ("Success", "ID")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    ID: int
    def __init__(self, Success: bool = ..., ID: _Optional[int] = ...) -> None: ...

class VideoUpdateRequest(_message.Message):
    __slots__ = ("ID", "Title", "Description", "Privacy", "Link")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    ID: int
    Title: str
    Description: str
    Privacy: _video_pb2.Privacy
    Link: str
    def __init__(self, ID: _Optional[int] = ..., Title: _Optional[str] = ..., Description: _Optional[str] = ..., Privacy: _Optional[_Union[_video_pb2.Privacy, str]] = ..., Link: _Optional[str] = ...) -> None: ...
