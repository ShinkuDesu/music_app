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
