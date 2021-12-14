from cover import Cover

class Album:
    name: str
    released: str
    tracks: int
    cover: Cover

    def __init__(self, name: str, released: str, track:int, cover: Cover) -> None:
        self.name = name
        self.released = released
        self.tracks = track
        self.cover = cover