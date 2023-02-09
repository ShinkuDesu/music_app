from sqlmodel import create_engine, SQLModel, Session
from models import user, music, playlist, links
from models import *

sqlite_file_name = "music_app.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


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


def get_session():
    with Session(engine) as session:
        yield session


if __name__ == "__main__":
    create_db_and_tables()
