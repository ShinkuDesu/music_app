from fastapi import APIRouter, Depends, HTTPException, status
from database.database import get_session
from sqlalchemy.orm import Session
from database.crud.music import MusicCrud
from database.models.music import MusicModel, MusicCreateModel


router = APIRouter(
    prefix='/music',
    tags=['music']
)


@router.get('/music/{playlist_id}', response_model=list[MusicModel])
async def get_music_list_by_playlist_id(playlist_id: int, session: Session = Depends(get_session)):
    response = MusicCrud(session).get_music_by_playlist_id(playlist_id)
    if response:
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Music not found'
        )


@router.get("/list", response_model=list[MusicModel], description='get music list from db')
async def get_music_list(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    response = MusicCrud(session).get_music_list(skip=skip, limit=limit)
    return response


@router.post('/create', response_model=MusicModel)
async def create_music(music_schema: MusicCreateModel, session: Session = Depends(get_session)):
    response = MusicCrud(session).create_music(music_schema)
    if response:
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Music not found'
        )


@router.delete('/delete/{music_id}')
async def delete_music_by_id(music_id: int, session: Session = Depends(get_session)):
    response = MusicCrud(session).delete_music_by_id(music_id)
    if response:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail='Successfully deleted music'
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Not found'
        )
