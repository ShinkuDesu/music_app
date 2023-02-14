from sqlmodel import select
from models.playlist import *
from models.music import *
from crud.base import CrudBase


class PlaylistCrud(CrudBase):
    async def get_playlist_by_id(self, playlist_id: int) -> Playlist | None:
        return await self.session.get(Playlist, playlist_id)

    async def get_playlist_list(self, offset: int = 0, limit: int = 100) -> list[Playlist]:
        stmt = select(Playlist).offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create_playlist(self, playlist: PlaylistCreate) -> Playlist:
        db_playlist = Playlist.from_orm(playlist)
        self.session.add(db_playlist)
        await self.session.commit()
        await self.session.refresh(db_playlist)
        return db_playlist
    
    async def delete_playlist_by_id(self, playlist_id: int) -> Playlist | None:
        return await self.session.get(Playlist, playlist_id)

    async def update_playlist(self, playlist_id: int, playlist: PlaylistUpdate) -> Playlist | None:
        db_playlist = await self.session.get(Playlist, playlist_id)
        if not db_playlist:
            return None
        playlist_data = playlist.dict(exclude_unset=True)
        for key, value in playlist_data.items():
            setattr(db_playlist, key, value)
        self.session.add(db_playlist)
        await self.session.commit()
        await self.session.refresh(db_playlist)
        return db_playlist

    async def add_music_into_playlist_by_id(self, playlist_id: int, music_id: int) -> Playlist | None:
        db_playlist = await self.session.get(Playlist, playlist_id)
        if not db_playlist:
            return None
        db_music = await self.session.get(Music, music_id)
        if not db_music:
            return None
        db_playlist.musics.append(db_music)
        self.session.add(db_playlist)
        await self.session.commit()
        await self.session.refresh(db_playlist)
        return db_playlist
