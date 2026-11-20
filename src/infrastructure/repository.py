import itertools

from src.domain.user import User


class UserRepository:
    def __init__(self) -> None:
        self._users: dict[str, User] = {}
        self._id_counter = itertools.count(1)

    def save(self, user: User) -> User:
        if user.id is None:
            user.id = next(self._id_counter)
        self._users[user.email] = user
        return user

    def get_by_email(self, email: str) -> User | None:
        return self._users.get(email)

    def list(self) -> list[User]:
        return list(self._users.values())
