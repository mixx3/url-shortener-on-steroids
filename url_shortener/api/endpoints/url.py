from fastapi import APIRouter
from url_shortener.api.schemas import UrlPostRequest, UrlPostResponse
from fastapi import Depends
from url_shortener.config import get_settings
from fastapi.exceptions import HTTPException
from url_shortener.service import InterfaceUrlService, get_url_service
import url_shortener.api.utils as utils
import url_shortener.service.exceptions as exc
from starlette import status


settings = get_settings()
url_router = APIRouter(prefix="/url", tags=["Url"])


@url_router.post(
    "/v1/",
    response_model=UrlPostResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "URL is not in valid format or wrong body format"
        },
        status.HTTP_400_BAD_REQUEST: {"description": "Error while accessing to URL"},
    },
)
async def make_short_suffix(
    request_url: UrlPostRequest,
    url_service: InterfaceUrlService = Depends(get_url_service),
):
    try:
        suffix = await url_service.make_suffix(request_url.long_url)
    except exc.InvalidUrl as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=repr(e))
    return UrlPostResponse(long_url=request_url.long_url, suffix=suffix)


@url_router.post(
    "/v2/",
    response_model=UrlPostResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "URL is not in valid format or wrong body format"
        },
        status.HTTP_400_BAD_REQUEST: {"description": "Error while accessing to URL"},
        status.HTTP_401_UNAUTHORIZED: {"description": "User unauthorized"}
    }
)
async def make_short_suffix_auth(
        request_url: UrlPostRequest,
        url_service: InterfaceUrlService = Depends(get_url_service),
        current_user=Depends(utils.get_current_user)
):
    try:
        suffix = await url_service.make_suffix(request_url.long_url, user_id=current_user.id)
    except exc.InvalidUrl as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=repr(e))
    return UrlPostResponse(long_url=request_url.long_url, suffix=suffix)


@url_router.get(
    "/v2/all",
    response_model=list[UrlPostResponse],
    status_code=status.HTTP_200_OK,
)
async def get_my_urls(
        url_service: InterfaceUrlService = Depends(get_url_service),
        current_user=Depends(utils.get_current_user)
):
    return url_service.get_urls_by_user_id(current_user.id)
