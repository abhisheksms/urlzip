from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException

from src.utils import shorten_url, store_url

app = FastAPI()
urlstore = {}


@app.get("/ping")
def root():
    return {"message": "ok"}


@app.get('/shorten')
def get_shortened_link(url: str):
    """
    Accepts url and returns it's shortened version
    """
    short_url = shorten_url(url.rstrip("/"))
    if short_url not in urlstore:
        store_url(url, short_url)
        urlstore[short_url] = url
    return f"http://localhost:8000/{short_url}"


@app.get('/{short_url}')
def redirect(short_url: str):
    """
    Redirects to original url
    """
    if short_url not in urlstore:
        raise HTTPException(status_code=404, detail='Provided link does not exist.')

    return RedirectResponse(url=urlstore[short_url])