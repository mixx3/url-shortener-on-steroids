from fastapi import APIRouter
from url_shortener.api.schemas import HealthResponse
from starlette import status

ping_router = APIRouter(tags=["Ping service"])


# redis-like simple health check


@ping_router.get(
    "/v1/health_check",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
)
async def health_check():
    return HealthResponse()
