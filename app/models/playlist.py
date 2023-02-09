from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
from .links import UserPlaylistLink, MusicPlaylistLink


if TYPE_CHECKING:
    from .user import User, UserRead
    from .music import Music, MusicRead


class PlaylistBase(SQLModel):
    title: str = Field(max_length=32)
    description: str | None = Field(max_length=265)


class Playlist(PlaylistBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    users: list['User'] = Relationship(back_populates='playlists', link_model=UserPlaylistLink)
    musics: list['Music'] = Relationship(back_populates='playlists', link_model=MusicPlaylistLink)


class PlaylistCreate(PlaylistBase):
    pass


class PlaylistUpdate(PlaylistBase):
    pass


class PlaylistRead(PlaylistBase):
    id: int


class PlaylistReadWithMusicsAndUsers(PlaylistRead):
    musics: list['MusicRead'] = []
    users: list['UserRead'] = []


class PlaylistReadWithMusic(PlaylistRead):
    music: list['MusicRead'] = []
