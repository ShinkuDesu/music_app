from sqlmodel import select
from models.playlist import *
from models.music import *
from models.user import *
from crud.base import CrudBase


class UserCrud(CrudBase):
    async def get_user_by_id(self, user_id: int) -> User | None:
        return await self.session.get(User, user_id)

    async def get_user_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        result = await self.session.execute(stmt)
        return result.scalar()
