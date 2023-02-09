from sqlmodel import Session, select
from models.playlist import *
from models.music import *
from fastapi import HTTPException


class PlaylistCrud:
    def __init__(self, session: Session):
        self.session = session

    def get_playlist_by_id(self, playlist_id: int) -> Playlist:
        db_playlist = self.session.get(Playlist, playlist_id)
        if not db_playlist:
            raise HTTPException(404, 'Playlist not found.')
        return db_playlist

    def get_playlist_list(self, offset: int = 0, limit: int = 100) -> list[Playlist]:
        return self.session.exec(select(Playlist).offset(offset).limit(limit)).all()

    def create_playlist(self, playlist: PlaylistCreate) -> Playlist:
        db_playlist = Playlist.from_orm(playlist)
        self.session.add(db_playlist)
        self.session.commit()
        self.session.refresh(db_playlist)
        return db_playlist
    
    def delete_playlist_by_id(self, playlist_id: int) -> dict:
        db_playlist = self.session.get(Playlist, playlist_id)
        if db_playlist:
            self.session.delete(db_playlist)
            self.session.commit()
            return {'ok': True}
        else:
            raise HTTPException(404, 'Playlist not found.')

    def update_playlist(self, playlist_id: int, playlist: PlaylistUpdate) -> Playlist:
        db_playlist = self.session.get(Playlist, playlist_id)
        if not db_playlist:
            raise HTTPException(status_code=404, detail='playlist not found.')
        playlist_data = playlist.dict(exclude_unset=True)
        for key, value in playlist_data.items():
            setattr(db_playlist, key, value)
        self.session.add(db_playlist)
        self.session.commit()
        self.session.refresh(db_playlist)
        return db_playlist

    def add_music(self, playlist_id: int, music_id: int) -> Playlist:
        db_playlist = self.session.get(Playlist, playlist_id)
        if not db_playlist:
            raise HTTPException(404, 'Playlist not found.')
        db_music = self.session.get(Music, music_id)
        if not db_music:
            raise HTTPException(404, 'Music not found.')
        db_playlist.musics.append(db_music)
        self.session.add(db_playlist)
        self.session.commit()
        self.session.refresh(db_playlist)
        return db_playlist

    def add_music_into_playlist_by_id(self, playlist_id: int, music_id: int) -> Playlist:
        db_playlist = self.session.get(Playlist, playlist_id)
        db_music = self.session.get(Music, music_id)
        if not db_playlist:
            raise HTTPException(404, 'Playlist not found.')
        if not db_music:
            raise HTTPException(404, 'Music not found.')
        db_playlist.musics.append(db_music)
        self.session.add(db_playlist)
        self.session.commit()
        self.session.refresh(db_playlist)
        return db_playlist
