from fastapi import FastAPI
from .ping import ping_router
from .url import url_router

app = FastAPI(description="Url shortener API")

app.include_router(ping_router)
app.include_router(url_router)
