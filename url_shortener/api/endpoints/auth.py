from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette import status
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from url_shortener.api.schemas import Token, RegistrationForm
from url_shortener.bootstrap import pg_auth_service
from url_shortener.service.auth_service import AuthService
import url_shortener.service.exceptions as exc


auth_router = APIRouter(tags=["Authentication"])
oauth2bearer = OAuth2PasswordBearer(tokenUrl='/authentication')


@auth_router.post(
    "/authentication",
    status_code=status.HTTP_200_OK,
    response_model=Token,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            'description': 'Incorrect params'
        }
    }
)
async def get_token(
    _: Request,
    form: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(pg_auth_service),
):
    try:
        user = await auth_service.authenticate_user(form.username, form.password)
    except exc.WrongPassword:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    except exc.NotRegistered:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not registered"
        )
    access_token = await auth_service.create_token(username=user.username)
    return Token(token=access_token)


@auth_router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            'description': 'Incorrect params'
        }
    }
)
async def register(
    _: Request,
    data: RegistrationForm,
    auth_service: AuthService = Depends(pg_auth_service),
) -> None:
    username, password = data.username, data.password
    try:
        await auth_service.registrate_user(username, password)
    except exc.AlreadyRegistered as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=repr(e))


@auth_router.get("/me")
async def get_current_user_info(
        _: Request,
        token: str = Depends(oauth2bearer),
):
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
