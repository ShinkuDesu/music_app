from sqlalchemy.orm import Session

from ..tables.music import MusicTable
from ..models.music import MusicCreateModel


class MusicCrud:
    def __init__(self, session: Session):
        self.session = session

    def get_music_by_id(self, music_id: int):
        return (
            self.session.query(MusicTable)
            .filter(MusicTable.id == music_id)
            .first()
        )

    def create_music(self, music: MusicCreateModel):
        db_music = MusicTable(**music.dict())
        self.session.add(db_music)
        self.session.commit()
        self.session.refresh(db_music)
        return db_music

    def delete_music_by_id(self, music_id: int) -> bool:
        result = (
            self.session.query(MusicTable)
            .filter(MusicTable.id == music_id)
            .delete()
        )
        self.session.commit()
        return bool(result)

    def get_music_by_playlist_id(self, playlist_id: int):
        return (
            self.session.query(MusicTable)
            .filter(MusicTable.playlist_id == playlist_id)
            .all()
        )

    def get_music_list(self, skip: int = 0, limit: int = 100):
        return (
            self.session.query(MusicTable)
            .offset(skip).limit(limit)
            .all()
        )
