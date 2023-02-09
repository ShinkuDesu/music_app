from sqlmodel import Field, SQLModel


class UserPlaylistLink(SQLModel, table=True):
    user_id: int | None = Field(
        default=None,
        foreign_key="user.id",
        primary_key=True,
    )
    playlist_id: int | None = Field(
        default=None,
        foreign_key="playlist.id",
        primary_key=True,
    )
    


class MusicPlaylistLink(SQLModel, table=True):
    music_id: int | None = Field(
        default=None,
        foreign_key="music.id",
        primary_key=True,
    )
    playlist_id: int | None = Field(
        default=None,
        foreign_key="playlist.id",
        primary_key=True,
    )
