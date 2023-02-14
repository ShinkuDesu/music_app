from fastapi import APIRouter, Depends, HTTPException
from database.database import get_session
from sqlmodel import Session
from sqlmodel.ext.asyncio.session import AsyncSession
from crud.music import MusicCrud
from models.music import *


router = APIRouter(
    prefix='/music',
    tags=['music']
)


@router.get("/{music_id}", response_model=MusicReadWithPlaylists)
async def get_music_by_id(music_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.get(Music, music_id)
    if not result: raise HTTPException(404,'Music not found')
    return result


@router.get("/", response_model=list[MusicReadWithPlaylists])
async def get_music_list(offset: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)) -> list[Music]:
    return await MusicCrud(session).get_music_list(offset, limit)


@router.post('/', response_model=MusicReadWithPlaylists)
async def create_music(music: MusicCreate, session: AsyncSession = Depends(get_session)) -> Music:
    return await MusicCrud(session).create_music(music)
    

@router.delete('/{music_id}')
async def delete_music_by_id(music_id: int, session: AsyncSession = Depends(get_session)) -> dict:
    result = await MusicCrud(session).delete_music_by_id(music_id)
    if not result: raise HTTPException(404, 'Music not found.')
    return {'ok': True}


@router.patch('/{music_id}', response_model=MusicReadWithPlaylists)
async def update_music(music_id: int, music: MusicUpdate, session: AsyncSession = Depends(get_session)) -> Music:
    result = await MusicCrud(session).update_music_by_id(music_id, music)
    if not result: raise HTTPException(404, 'Music not found.')
    return result
