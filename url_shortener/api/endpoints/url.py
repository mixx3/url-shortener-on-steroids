from fastapi import APIRouter
from url_shortener.api.schemas import UrlPostRequest, UrlPostResponse
from fastapi import Depends
from fastapi.exceptions import HTTPException
from url_shortener.service import UrlService
from url_shortener.bootstrap import pg_url_service
from url_shortener.service.exceptions import InvalidUrl
from starlette import status


url_router = APIRouter(prefix="/url", tags=["Url"])


@url_router.post(
    "/v1/",
    response_model=UrlPostResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "URL is not valid or wrong body format"
        }
    },
)
async def make_short_suffix(
    request_url: UrlPostRequest, url_service: UrlService = Depends(pg_url_service)
):
    try:
        suffix = await url_service.make_suffix(request_url.long_url)
    except InvalidUrl as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=repr(e))
    return UrlPostResponse(short_url=suffix)
