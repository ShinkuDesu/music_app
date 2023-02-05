from pydantic import BaseModel
from models.music import MusicModel


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
