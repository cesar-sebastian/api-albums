import requests
from multimedia import Multimedia
from artist import Artist
from album import Album
from cover import Cover
from fastapi import HTTPException
from secrets import spotify_token

class Spotify(Multimedia):
    URL_SEARCH = 'https://api.spotify.com/v1/search'
    URL_ALBUMS = 'https://api.spotify.com/v1/artists/_id_/albums'    

    def __init__(self) -> None:
        self.headers =  {
            "Authorization": f"Bearer {spotify_token}"
        }

    def get(self, url: str, params):
        try:
            response = requests.get(url=url, params=params, headers=self.headers)
            print(response)
            if response.ok:
                return response.json()
            else:
                raise HTTPException(status_code=400, detail="Bad Response ko")
        except requests.exceptions.Timeout:
            raise HTTPException(status_code=400, detail="Bad Response")

    def fetch_artist(self, name: str) -> Artist:
        '''
        - devuelve FALSE or Artist object        
        curl -X "GET" "https://api.spotify.com/v1/search?q=artist%3APedro&type=artist&market=ES&limit=10&offset=5" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer "
        - Que pasa si vienen muchos resultados? se toma el primero o no se devuelve nada?    
        - Debo devolver album si y solo si el artista tiene precision 100%
        - Otra opcion es, si hay muchos devolver una lista pequeña de artistas recomendados.
        '''
        p = (('q', f'artist:{name}'), ('type', 'artist'), ('market', 'ES'), ('limit', '50'),('offset', '0'))        

        json_resp = self.get(self.URL_SEARCH, p)
        
        if 'artists' not in json_resp:
            raise HTTPException(status_code=404, detail="Artist not found - artists")
        
        if 'items' not in json_resp['artists']:
            raise HTTPException(status_code=404, detail="Artist not found - items")
        
        for a in json_resp['artists']['items']:
            return Artist(a['id'], a['name'])
    
    def fetch_album_artist(self, artist: Artist) -> Artist:
        p = (('include_groups', 'single'), ('market', 'ES'), ('limit', '50'),('offset', '0'))
        json_resp = self.get(self.URL_ALBUMS.replace('_id_', artist.id), p)

        if 'items' not in json_resp:
            raise HTTPException(status_code=404, detail="Artist's albums not found")
        
        for album_data in json_resp['items']:
            if 'name' not in album_data or 'total_tracks' not in album_data or 'release_date' not in album_data:
                raise HTTPException(status_code=404, detail="Lack information in albums - name, total_tracks, release_date")
            
            if 'images' not in album_data:
                raise HTTPException(status_code=404, detail="Lack information in albums - images")

            '''
            - Solo se obtiene un elemento images - cover, como indica la estructura de respuesta, se toma el primero
            '''
            cover = Cover(album_data['images'][0]['height'], album_data['images'][0]['width'], album_data['images'][0]['url'])

            album = Album(album_data['name'], album_data['release_date'], album_data['total_tracks'], cover)
            artist.add_album(album)
        
        return artist
                
    def fetch_albums(self, name: str):
        artist = self.fetch_artist(name)
        self.fetch_album_artist(artist)

        return artist.albums