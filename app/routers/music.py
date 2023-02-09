from fastapi import APIRouter, Depends, HTTPException, status
from database.database import get_session
from sqlmodel import Session
from crud.music import MusicCrud
from models.music import *


router = APIRouter(
    prefix='/music',
    tags=['music']
)


@router.get("/{music_id}", response_model=MusicReadWithPlaylists)
async def get_music_by_id(music_id: int, session: Session = Depends(get_session)):
    response = session.get(Music, music_id)
    if response:
        return response
    else:
        raise HTTPException(404,'Music not found')


@router.get("/", response_model=list[MusicReadWithPlaylists])
async def get_music_list(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)) -> list[Music]:
    return MusicCrud(session).get_music_list(offset, limit)


@router.post('/', response_model=MusicReadWithPlaylists)
async def create_music(music: MusicCreate, session: Session = Depends(get_session)) -> Music:
    return MusicCrud(session).create_music(music)
    

@router.delete('/{music_id}')
async def delete_music_by_id(music_id: int, session: Session = Depends(get_session)) -> dict:
    return MusicCrud(session).delete_music_by_id(music_id)


@router.patch('/{music_id}', response_model=MusicReadWithPlaylists)
def update_music(music_id: int, music: MusicUpdate, session: Session = Depends(get_session)) -> Music:
    return MusicCrud(session).update_music_by_id(music_id, music)
