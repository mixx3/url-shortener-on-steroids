from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from url_shortener.config import get_settings
from url_shortener.bootstrap import pg_auth_service
from url_shortener.service.auth_service import AuthService

settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def create_token(**kwargs):
    payload = kwargs.copy()
    expire_date = datetime.utcnow() + settings.EXPIRY_TIMEDELTA
    payload.update({"exp": expire_date})
    token = jwt.encode(payload, key=settings.JWT_KEY)
    return token


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(pg_auth_service),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await auth_service.get_user(username)
    if user is None:
        raise credentials_exception
    return user
