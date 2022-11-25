from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from typing import Type
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from url_shortener.api.schemas import Token, RegistrationForm
from url_shortener.bootstrap import pg_auth_service
from url_shortener.service.auth_service import AuthService
from url_shortener.service.exceptions import AlreadyRegistered
import url_shortener.api.utils as utils

auth_router = APIRouter(tags=["Authentication"])


@auth_router.post(
    "/authentication", status_code=status.HTTP_200_OK, response_model=Token
)
async def get_token(
    _: Request,
    form: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(pg_auth_service),
):
    pass


@auth_router.post("/register", status_code=status.HTTP_201_CREATED, response_model=None)
async def register(
    _: Request,
    data: RegistrationForm,
    auth_serice: AuthService = Depends(pg_auth_service),
):
    username, password = data.username, data.password
    try:
        await auth_serice.registrate_user(username, password)
    except AlreadyRegistered as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=repr(e))
