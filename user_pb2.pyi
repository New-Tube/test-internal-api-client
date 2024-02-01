import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserRequest(_message.Message):
    __slots__ = ("ID", "Nickname")
    ID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    ID: int
    Nickname: str
    def __init__(self, ID: _Optional[int] = ..., Nickname: _Optional[str] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("ID", "Name", "Surname", "Nickname", "PasswordHash", "CreatedAt", "EditedAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORDHASH_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    EDITEDAT_FIELD_NUMBER: _ClassVar[int]
    ID: int
    Name: str
    Surname: str
    Nickname: str
    PasswordHash: int
    CreatedAt: int
    EditedAt: int
    def __init__(self, ID: _Optional[int] = ..., Name: _Optional[str] = ..., Surname: _Optional[str] = ..., Nickname: _Optional[str] = ..., PasswordHash: _Optional[int] = ..., CreatedAt: _Optional[int] = ..., EditedAt: _Optional[int] = ...) -> None: ...

class UserUpdateRequest(_message.Message):
    __slots__ = ("ID", "Name", "Surname", "Nickname", "PasswordHash")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORDHASH_FIELD_NUMBER: _ClassVar[int]
    ID: int
    Name: str
    Surname: str
    Nickname: str
    PasswordHash: int
    def __init__(self, ID: _Optional[int] = ..., Name: _Optional[str] = ..., Surname: _Optional[str] = ..., Nickname: _Optional[str] = ..., PasswordHash: _Optional[int] = ...) -> None: ...

class UserCreateRequest(_message.Message):
    __slots__ = ("Nickname", "PasswordHash", "Name", "Surname")
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORDHASH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    Nickname: str
    PasswordHash: int
    Name: str
    Surname: str
    def __init__(self, Nickname: _Optional[str] = ..., PasswordHash: _Optional[int] = ..., Name: _Optional[str] = ..., Surname: _Optional[str] = ...) -> None: ...
