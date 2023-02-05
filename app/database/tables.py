from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base


# from .playlist import PlaylistTable
class UserTable(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    hashed_password: Mapped[str]

    playlists: Mapped[list['PlaylistTable']] = relationship()


# from .user import UserTable
# from .music import MusicTable
class PlaylistTable(Base):
    __tablename__ = 'playlist'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    user: Mapped['UserTable'] = relationship()
    musics: Mapped[list['MusicTable']] = relationship()


# from .music import PlaylistTable
class MusicTable(Base):
    __tablename__ = 'music'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    author: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    duration_sec: Mapped[int] = mapped_column()

    playlist_id: Mapped[int] = mapped_column(ForeignKey('playlist.id'))

    playlist: Mapped['PlaylistTable'] = relationship()
