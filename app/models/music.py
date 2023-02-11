from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
from .links import MusicPlaylistLink


if TYPE_CHECKING:
    from .playlist import Playlist, PlaylistRead


class MusicBase(SQLModel):
    title: str = Field(max_length=64)
    author: str = Field(max_length=64)
    duration: int


class Music(MusicBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    playlists: list['Playlist'] = Relationship(
        back_populates='musics',
        link_model=MusicPlaylistLink,
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    

class MusicCreate(MusicBase):
    pass

class MusicUpdate(MusicBase):
    pass


class MusicRead(MusicBase):
    id: int


class MusicReadWithPlaylists(MusicRead, lazy=False):
    playlists: list['PlaylistRead'] = []
