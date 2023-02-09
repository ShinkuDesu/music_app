from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.responses import 
from database.database import get_session
from crud.playlist import PlaylistCrud
from models.playlist import *
from sqlmodel import Session


router = APIRouter(
    prefix='/playlist',
    tags=['playlist'],
)


@router.get('/{playlist_id}', response_model=PlaylistReadWithMusicsAndUsers)
async def get_playlist_by_id(playlist_id: int, session: Session = Depends(get_session)) -> Playlist:
    return PlaylistCrud(session).get_playlist_by_id(playlist_id)


@router.get('/', response_model=list[PlaylistReadWithMusicsAndUsers], description='get a list of playlists')
async def get_playlist_list(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return PlaylistCrud(session).get_playlist_list(offset=offset, limit=limit)


@router.post('/', response_model=PlaylistReadWithMusicsAndUsers)
def create_playlist(playlist: PlaylistCreate, session: Session = Depends(get_session)) -> Playlist:
    return PlaylistCrud(session).create_playlist(playlist)


@router.delete('/{playlist_id}')
def delete_playlist_by_id(playlist_id: int, session: Session = Depends(get_session)) -> dict:
    return PlaylistCrud(session).delete_playlist_by_id(playlist_id)


@router.patch('/{playlist_id}', response_model=PlaylistReadWithMusicsAndUsers)
def update_playlist(playlist_id: int, playlist: PlaylistUpdate, session: Session = Depends(get_session)) -> Playlist:
    return PlaylistCrud(session).update_playlist(playlist_id, playlist)


@router.post('/music{playlist_id}', response_model=PlaylistReadWithMusicsAndUsers)
def add_music_into_playlist_by_id(playlist_id: int, music_id: int, session: Session = Depends(get_session)) -> Playlist:
    return PlaylistCrud(session).add_music_into_playlist_by_id(playlist_id, music_id)
