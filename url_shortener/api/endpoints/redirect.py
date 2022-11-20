from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from starlette import status
from fastapi import Depends
from url_shortener.db import PgSession
from url_shortener.service import UrlService
from sqlalchemy.orm import Session


redirect_router = APIRouter(tags=['Redirect'])


@redirect_router.get(
    "/{suffix}",
    response_class=RedirectResponse,
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    responses={status.HTTP_404_NOT_FOUND: {"detail": "suffix not found"}}
)
async def redirect_to_long(suffix: str,
                           url_service: UrlService = Depends(),
                           ):
    long_url = await url_service.get_long_url(suffix)
    return RedirectResponse

