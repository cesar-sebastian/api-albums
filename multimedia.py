from abc import ABC, abstractmethod

class Multimedia(ABC):
    @abstractmethod
    def fetch_albums(self, name):
        '''Fetch albums by name'''