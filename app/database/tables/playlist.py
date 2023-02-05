from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..database import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .user import UserTable
    from .music import MusicTable


class PlaylistTable(Base):
    __tablename__ = 'playlist'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    user: Mapped['UserTable'] = relationship()
    musics: Mapped[list['MusicTable']] = relationship()
