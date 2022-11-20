from .base import app
from starlette import status
from starlette.exceptions import HTTPException


@app.exception_handler(Exception)
def mock_exception_handlers():
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Server error"
    )
