from fastapi import FastAPI
from utils import shorten_url

app = FastAPI()

@app.get("/ping")
def root():
    return {"message": "ok"}

@app.get('/shorten')
def get_original_link(url: str):
    """
    Accepts url and returns it's shortened version
    """
    short_url = shorten_url(url)
    return short_url