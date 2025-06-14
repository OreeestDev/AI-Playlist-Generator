from venv import create

from fastapi import FastAPI
from pydantic import BaseModel
from Promts import create_playlist
from Deezer import Deezer_Promt


app = FastAPI()


class Promt(BaseModel):
    content: str


@app.post("/playlist")
def promt(data: Promt):
    tracks = create_playlist(data.content)
    playlist = Deezer_Promt(tracks)
    return {"playlist": playlist}








