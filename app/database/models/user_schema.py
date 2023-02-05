from pydantic import BaseModel
from models.playlist import PlaylistModel


class UserBaseModel(BaseModel):
    username: str


class UserModel(UserBaseModel):
    id: int
    playlists: list[PlaylistModel]

    class Config:
        orm_mode = True


class UserCreateModel(UserBaseModel):
    password: str
