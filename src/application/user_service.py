from src.domain.user import User
from src.infrastructure.repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def register_user(self, username: str, email: str) -> User:
        if self.repository.get_by_email(email):
            raise ValueError("Email already registered")
        user = User(username=username, email=email)
        return self.repository.save(user)

    def get_users(self) -> list[User]:
        return self.repository.list()
