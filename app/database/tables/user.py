from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..database import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .playlist import PlaylistTable


class UserTable(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    hashed_password: Mapped[str]

    playlists: Mapped[list['PlaylistTable']] = relationship()


