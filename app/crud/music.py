from sqlmodel import Session, select
from fastapi import HTTPException
from models.music import *
from models.playlist import *


class MusicCrud:
    def __init__(self, session: Session):
        self.session = session
    
    def get_music_list(self, offset: int = 0, limit: int = 100) -> list[Music]:
        return self.session.exec(select(Music).offset(offset).limit(limit)).all()

    def create_music(self, music: MusicCreate) -> Music:
        db_music = Music.from_orm(music)
        self.session.add(db_music)
        self.session.commit()
        self.session.refresh(db_music)
        return db_music
    
    def delete_music_by_id(self, music_id: int) -> dict:
        try:
            db_music = self.session.exec(select(Music).where(Music.id == music_id)).one()
            self.session.delete(db_music)
            return {'ok': True}
        except:
            raise HTTPException(404, 'Music not found.')

    def get_music_by_id(self, music_id: int) -> Music:
        result = self.session.get(Music, music_id)
        if result:
            return result
        else:
            raise HTTPException(404, 'Music not found.')

    def update_music_by_id(self, music_id: int, music: MusicUpdate) -> Music:
        db_music = self.session.get(Music, music_id)
        if not db_music:
            raise HTTPException(status_code=404, detail="Music not found.")
        music_data = music.dict(exclude_unset=True)
        for key, value in music_data.items():
            setattr(db_music, key, value)
        self.session.add(db_music)
        self.session.commit()
        self.session.refresh(db_music)
        return db_music
