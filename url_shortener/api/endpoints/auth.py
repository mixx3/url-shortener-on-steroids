from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette import status
from fastapi.requests import Request
from typing import Type
from fastapi.exceptions import HTTPException
from url_shortener.service import InterfaceAuthService, get_auth_service
import url_shortener.api.schemas as schemas
import url_shortener.service.exceptions as exc
import url_shortener.api.utils as utils
from url_shortener.config import get_settings


settings = get_settings()
auth_router = APIRouter(tags=["Authentication"])
oauth2bearer = OAuth2PasswordBearer(tokenUrl="token")


@auth_router.post(
    "/token",
    status_code=status.HTTP_200_OK,
    response_model=schemas.Token,
    responses={status.HTTP_401_UNAUTHORIZED: {"description": "Incorrect params"}},
)
async def get_token(
    _: Request,
    form: OAuth2PasswordRequestForm = Depends(),
    auth_service: InterfaceAuthService = Depends(get_auth_service),
):
    try:
        user = await auth_service.authenticate_user(form.username, form.password)
    except exc.WrongPassword:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except exc.NotRegistered:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = await utils.create_token(username=user.username)
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
    responses={status.HTTP_400_BAD_REQUEST: {"description": "Incorrect params"}},
)
async def register(
    _: Request,
    data: schemas.RegistrationForm,
    auth_service: InterfaceAuthService = Depends(get_auth_service),
) -> None:
    username, password = data.username, data.password
    try:
        await auth_service.registrate_user(username, password)
    except exc.AlreadyRegistered as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=repr(e))


@auth_router.get(
    "/whoami",
    status_code=status.HTTP_200_OK,
    response_model=schemas.User,
    responses={status.HTTP_401_UNAUTHORIZED: {"detail": "Unauthorized"}},
)
async def get_current_user_info(
    _: Request, current_user=Depends(utils.get_current_user)
):
    return schemas.User(id=current_user.id, username=current_user.username)
