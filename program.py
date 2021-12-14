from multimedia import Multimedia

class Program:
    def __init__(self, multimedia: Multimedia) -> None:
        self.multimedia = multimedia
    
    def fetch_album(self, name: str):
        return self.multimedia.fetch_albums(name)