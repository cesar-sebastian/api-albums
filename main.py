from spotify import Spotify
from program import Program
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/albums/")
def get_albums(q: str = ''):
    spotify = Spotify()
    program = Program(spotify)    
    return program.fetch_album(q)