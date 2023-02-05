from pydantic import BaseModel




class MusicBaseModel(BaseModel):
    title: str
    author: str
    duration_sec: int
    url: str


class MusicModel(MusicBaseModel):
    id: int

    class Config:
        orm_mode = True

    
class MusicCreateModel(MusicBaseModel):
    playlist_id: int

class PlaylistBaseModel(BaseModel):
    title: str

    class Config:
        orm_mode = True


class PlaylistModel(PlaylistBaseModel):
    id: int
    musics: list[MusicModel]

    class Config:
        orm_mode = True


class PlaylistCreateModel(PlaylistBaseModel):
    user_id: int

class UserBaseModel(BaseModel):
    username: str


class UserModel(UserBaseModel):
    id: int
    playlists: list[PlaylistModel]

    class Config:
        orm_mode = True


class UserCreateModel(UserBaseModel):
    password: str