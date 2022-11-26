from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from url_shortener.config import get_settings
from .ping import ping_router
from .url import url_router
from .redirect import redirect_router
from .auth import auth_router


settings = get_settings()

app = FastAPI(description="Url shortener API", title="Url shortener API")

app.include_router(ping_router)
app.include_router(url_router)
app.include_router(redirect_router)
app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)
