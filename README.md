# Api Search Albums

## Consideraciones

* Se toma el primer artista que coincide con la busqueda realizada (limit = 50).
* Se toma la primera pagina de albums del artista (limit = 50).
* Se mapeo el nodo cover con el nodo images (es una lista) de Spotify, y se toma solo el primer valor como indica la estructura.

## Run projets

### Set access token

Ingresar a **secrets.py** y darle valor a la variable **spotify_token**

### Install projects

```console
pip install -r requirements.txt
```

```console
uvicorn main:app --reload
```

Ir a

```console
http://localhost:8000/docs
```