from fastapi import APIRouter, Depends, HTTPException, status
from database.database import get_session
from sqlalchemy.orm import Session
from crud.playlist import PlaylistCrud
from models.playlist import PlaylistModel


router = APIRouter(
    prefix='/playlist',
    tags=['playlist'],
)

@router.get('/list/{user_id}', response_model=PlaylistModel)
async def get_playlist_list_by_user_id(user_id: int, skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    result = PlaylistCrud(session).get_playlist_list_by_user_id(user_id, skip=skip, limit=limit)
    return result


@router.get('/list', response_model=list[PlaylistModel], description='get a list of playlists')
async def get_playlist_list(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    result = PlaylistCrud(session).get_playlist_list(skip=skip, limit=limit)
    return result
