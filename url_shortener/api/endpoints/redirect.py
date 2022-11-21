from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from starlette import status
from fastapi import Depends
from url_shortener.service import UrlService
from url_shortener.bootstrap import pg_url_service


redirect_router = APIRouter(tags=["Redirect"])


@redirect_router.get(
    "/{suffix}",
    response_class=RedirectResponse,
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    responses={status.HTTP_404_NOT_FOUND: {"detail": "suffix not found"}},
)
async def redirect_to_long(
    suffix: str,
    url_service: UrlService = Depends(pg_url_service),
):
    long_url = await url_service.get_long_url(suffix)
    if long_url:
        return RedirectResponse(long_url)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="suffix not found"
        )
