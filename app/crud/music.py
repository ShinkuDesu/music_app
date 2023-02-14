from sqlmodel import select
from models.music import *
from models.playlist import *
from crud.base import CrudBase


class MusicCrud(CrudBase):
    async def get_music_list(self, offset: int = 0, limit: int = 100) -> list[Music]:
        stmt = select(Music).offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create_music(self, music: MusicCreate) -> Music:
        db_music = Music.from_orm(music)
        self.session.add(db_music)
        await self.session.commit()
        await self.session.refresh(db_music)
        return db_music
    
    async def delete_music_by_id(self, music_id: int) -> bool:
        music_db = await self.session.get(Music, music_id)
        if not music_db:
            return False
        await self.session.delete(music_db)
        await self.session.commit()
        return True

    async def get_music_by_id(self, music_id: int) -> Music | None:
        return await self.session.get(Music, music_id)

    async def update_music_by_id(self, music_id: int, music: MusicUpdate) -> Music | None:
        db_music = await self.session.get(Music, music_id)
        if not db_music: return None
        music_data = music.dict(exclude_unset=True)
        for key, value in music_data.items():
            setattr(db_music, key, value)
        self.session.add(db_music)
        await self.session.commit()
        await self.session.refresh(db_music)
        return db_music
