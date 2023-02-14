from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.responses import 
from database.database import get_session
from crud.playlist import PlaylistCrud
from models.playlist import *
from sqlmodel.ext.asyncio.session import AsyncSession


router = APIRouter(
    prefix='/playlist',
    tags=['playlist'],
)


@router.get('/{playlist_id}', response_model=PlaylistReadWithMusicsAndUsers)
async def get_playlist_by_id(playlist_id: int, session: AsyncSession = Depends(get_session)) -> Playlist:
    result =  await PlaylistCrud(session).get_playlist_by_id(playlist_id)
    if not result: raise HTTPException(404, 'Playlist not found.')
    return result


@router.get('/', response_model=list[PlaylistReadWithMusicsAndUsers])
async def get_playlist_list(offset: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)):
    return await PlaylistCrud(session).get_playlist_list(offset=offset, limit=limit)


@router.post('/', response_model=PlaylistReadWithMusicsAndUsers)
async def create_playlist(playlist: PlaylistCreate, session: AsyncSession = Depends(get_session)) -> Playlist:
    return await PlaylistCrud(session).create_playlist(playlist)


@router.delete('/{playlist_id}')
async def delete_playlist_by_id(playlist_id: int, session: AsyncSession = Depends(get_session)) -> dict:
    result = await PlaylistCrud(session).delete_playlist_by_id(playlist_id)
    if not result: raise HTTPException(404, 'Playlist not found.')
    return {'ok': True}


@router.patch('/{playlist_id}', response_model=PlaylistReadWithMusicsAndUsers)
async def update_playlist(playlist_id: int, playlist: PlaylistUpdate, session: AsyncSession = Depends(get_session)) -> Playlist:
    result = await PlaylistCrud(session).update_playlist(playlist_id, playlist)
    if not result: raise HTTPException(404, 'Playlist not found.')
    return result


@router.post('/music{playlist_id}', response_model=PlaylistReadWithMusicsAndUsers)
async def add_music_into_playlist_by_id(playlist_id: int, music_id: int, session: AsyncSession = Depends(get_session)) -> Playlist:
    result = await PlaylistCrud(session).add_music_into_playlist_by_id(playlist_id, music_id)
    if not result: raise HTTPException(404, 'Playlist not found.')
    return result
