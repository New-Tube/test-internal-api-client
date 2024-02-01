from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StatusResponse(_message.Message):
    __slots__ = ("Success", "Message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    Message: str
    def __init__(self, Success: bool = ..., Message: _Optional[str] = ...) -> None: ...

class ReactionRequest(_message.Message):
    __slots__ = ("UserID", "ID")
    USERID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    UserID: int
    ID: int
    def __init__(self, UserID: _Optional[int] = ..., ID: _Optional[int] = ...) -> None: ...

class ReactionResponse(_message.Message):
    __slots__ = ("IsLike", "IsDislike")
    ISLIKE_FIELD_NUMBER: _ClassVar[int]
    ISDISLIKE_FIELD_NUMBER: _ClassVar[int]
    IsLike: bool
    IsDislike: bool
    def __init__(self, IsLike: bool = ..., IsDislike: bool = ...) -> None: ...

class UpdateReactionRequest(_message.Message):
    __slots__ = ("ID", "UserID", "IsLike", "IsDislike")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    ISLIKE_FIELD_NUMBER: _ClassVar[int]
    ISDISLIKE_FIELD_NUMBER: _ClassVar[int]
    ID: int
    UserID: int
    IsLike: bool
    IsDislike: bool
    def __init__(self, ID: _Optional[int] = ..., UserID: _Optional[int] = ..., IsLike: bool = ..., IsDislike: bool = ...) -> None: ...
