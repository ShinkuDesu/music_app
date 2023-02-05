import uvicorn

from fastapi import FastAPI
from routers import music, playlist
from database.database import Base, engine


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(playlist.router)
app.include_router(music.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
