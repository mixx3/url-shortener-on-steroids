from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm


admin_router = APIRouter(tags=["Admin router"], prefix="/admin")


@admin_router.get("/urls")
def get_urls():
    pass


@admin_router.get("/users")
def get_users():
    pass
