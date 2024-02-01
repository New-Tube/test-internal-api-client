import video_pb2 as _video_pb2
import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoResponse(_message.Message):
    __slots__ = ("ID", "UserID", "Title", "Description", "Privacy", "Link", "Likes", "Dislikes", "CreatedAt", "EditedAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    DISLIKES_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    EDITEDAT_FIELD_NUMBER: _ClassVar[int]
    ID: int
    UserID: int
    Title: str
    Description: str
    Privacy: _video_pb2.Privacy
    Link: str
    Likes: int
    Dislikes: int
    CreatedAt: int
    EditedAt: int
    def __init__(self, ID: _Optional[int] = ..., UserID: _Optional[int] = ..., Title: _Optional[str] = ..., Description: _Optional[str] = ..., Privacy: _Optional[_Union[_video_pb2.Privacy, str]] = ..., Link: _Optional[str] = ..., Likes: _Optional[int] = ..., Dislikes: _Optional[int] = ..., CreatedAt: _Optional[int] = ..., EditedAt: _Optional[int] = ...) -> None: ...

class VideoStreamRequest(_message.Message):
    __slots__ = ("ID", "UserID", "Quality")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    ID: int
    UserID: int
    Quality: str
    def __init__(self, ID: _Optional[int] = ..., UserID: _Optional[int] = ..., Quality: _Optional[str] = ...) -> None: ...
