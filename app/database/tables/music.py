from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .playlist import PlaylistTable


class MusicTable(Base):
    __tablename__ = 'music'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    author: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    duration_sec: Mapped[int] = mapped_column()

    playlist_id: Mapped[int] = mapped_column(ForeignKey('playlist.id'))

    playlist: Mapped['PlaylistTable'] = relationship()
