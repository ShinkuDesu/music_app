from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING
from .links import UserPlaylistLink

if TYPE_CHECKING:
    from .playlist import Playlist, PlaylistRead


class UserBase(SQLModel):
    username: str = Field(max_length=64)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    playlists: list['Playlist'] = Relationship(
        back_populates='users',
        link_model=UserPlaylistLink,
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    hashed_password: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int


class UserReadWithPlaylists(UserRead):
    playlists: list['PlaylistRead'] = []
