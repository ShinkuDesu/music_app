from sqlalchemy.orm import Session
from database.tables import PlaylistTable


class PlaylistCrud:
    def __init__(self, session: Session):
        self.session = session

    def get_playlist_list(self, skip: int = 0, limit: int = 100):
        return (
            self.session.query(PlaylistTable)
            .offset(skip).limit(limit)
            .all()
        )

    def get_playlist_list_by_user_id(self, user_id: int, skip: int = 0, limit: int = 100):
        return (self.session.query(PlaylistTable)
            .where(PlaylistTable.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
