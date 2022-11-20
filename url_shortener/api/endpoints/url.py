from fastapi import APIRouter
from url_shortener.api.schemas import UrlPostRequest, UrlPostResponse
from starlette import status


url_router = APIRouter(prefix='/url')


@url_router.post(
    "/",
    response_model=UrlPostResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "URL is not valid or wrong body format"
        }
    }
)
async def make_short_suffix(long_url: UrlPostRequest):
    pass
