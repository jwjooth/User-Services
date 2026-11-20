from fastapi import APIRouter, Depends, HTTPException

from src.application.user_service import UserService
from src.domain.user import User
from src.infrastructure.repository import UserRepository

router = APIRouter()

_repo = UserRepository()
_service = UserService(_repo)


def get_user_service() -> UserService:
    return _service


@router.post("/", response_model=User)
def create_user(
    username: str, email: str, service: UserService = Depends(get_user_service)
) -> User:
    try:
        return service.register_user(username, email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/", response_model=list[User])
def get_users(service: UserService = Depends(get_user_service)) -> list[User]:
    return service.get_users()
