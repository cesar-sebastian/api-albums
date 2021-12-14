from typing import List
from album import Album

class Artist(object):
    id: str
    name: str
    albums: List[Album]
    
    def __init__(self, id: str, name: str) -> None:
        self.id, self.name, self.albums  = id, name, []
    
    def add_album(self, album: Album):
        self.albums.append(album)

    @staticmethod
    def from_json(cls, json_string):        
        return cls(**json_string)

    def __repr__(self) -> str:
        return f'<Artist { self.name }>'