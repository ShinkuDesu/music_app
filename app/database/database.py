from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from models import user, music, playlist
from models import *


sqlite_file_name = "music_app.db"
sqlite_url = f"sqlite+aiosqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_async_engine(sqlite_url, connect_args=connect_args)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


def update_all_refs():
    music.MusicReadWithPlaylists.update_forward_refs(
        PlaylistRead=playlist.PlaylistRead
    )
    user.UserReadWithPlaylists.update_forward_refs(
        PlaylistRead=playlist.PlaylistRead
    )
    playlist.PlaylistReadWithMusicsAndUsers.update_forward_refs(
        MusicRead=music.MusicRead,
        UserRead=user.UserRead,
    )


async def get_session():
    async with AsyncSession(bind=engine) as session:
        yield session
