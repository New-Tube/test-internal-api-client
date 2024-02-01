import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommentRequest(_message.Message):
    __slots__ = ("ID",)
    ID_FIELD_NUMBER: _ClassVar[int]
    ID: int
    def __init__(self, ID: _Optional[int] = ...) -> None: ...

class CommentCreateRequest(_message.Message):
    __slots__ = ("UserID", "VideoID", "CommentID", "Text")
    USERID_FIELD_NUMBER: _ClassVar[int]
    VIDEOID_FIELD_NUMBER: _ClassVar[int]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    UserID: int
    VideoID: int
    CommentID: int
    Text: str
    def __init__(self, UserID: _Optional[int] = ..., VideoID: _Optional[int] = ..., CommentID: _Optional[int] = ..., Text: _Optional[str] = ...) -> None: ...

class CommentResponse(_message.Message):
    __slots__ = ("ID", "Text", "VideoID", "CommentID", "UserID", "Likes", "Dislikes", "CreatedAt", "EditedAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEOID_FIELD_NUMBER: _ClassVar[int]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    DISLIKES_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    EDITEDAT_FIELD_NUMBER: _ClassVar[int]
    ID: int
    Text: str
    VideoID: int
    CommentID: int
    UserID: int
    Likes: int
    Dislikes: int
    CreatedAt: int
    EditedAt: int
    def __init__(self, ID: _Optional[int] = ..., Text: _Optional[str] = ..., VideoID: _Optional[int] = ..., CommentID: _Optional[int] = ..., UserID: _Optional[int] = ..., Likes: _Optional[int] = ..., Dislikes: _Optional[int] = ..., CreatedAt: _Optional[int] = ..., EditedAt: _Optional[int] = ...) -> None: ...

class GetManyRequest(_message.Message):
    __slots__ = ("VideoID", "CommentID", "Offset", "Limit")
    VIDEOID_FIELD_NUMBER: _ClassVar[int]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    VideoID: int
    CommentID: int
    Offset: int
    Limit: int
    def __init__(self, VideoID: _Optional[int] = ..., CommentID: _Optional[int] = ..., Offset: _Optional[int] = ..., Limit: _Optional[int] = ...) -> None: ...

class GetManyResponse(_message.Message):
    __slots__ = ("Count", "Comments")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    Count: int
    Comments: _containers.RepeatedCompositeFieldContainer[CommentResponse]
    def __init__(self, Count: _Optional[int] = ..., Comments: _Optional[_Iterable[_Union[CommentResponse, _Mapping]]] = ...) -> None: ...
