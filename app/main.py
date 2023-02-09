import uvicorn

from fastapi import FastAPI
from routers import music, playlist, user
from database.database import create_db_and_tables, update_all_refs


app = FastAPI()


update_all_refs()
app.include_router(playlist.router)
app.include_router(music.router)
app.include_router(user.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
