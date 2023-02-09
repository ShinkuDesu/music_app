from sqlmodel import Session, select
from models.playlist import *
from models.music import *
from models.user import *
from fastapi import HTTPException


class UserCrud:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, user_id: int) -> User:
        db_user = self.session.get(User, user_id)
        if not db_user:
            raise HTTPException(400, 'Incorrect username or password')
        return db_user

    def get_user_by_username(self, username: str) -> User | None:
        return self.session.exec(select(User).where(User.username == username)).first()
        
