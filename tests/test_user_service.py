from fastapi.testclient import TestClient

from src.application.user_service import UserService
from src.infrastructure.repository import UserRepository
from src.main import app


def test_register_user():
    repo = UserRepository()
    service = UserService(repo)
    user = service.register_user("test", "test@example.com")
    assert user.id == 1
    assert user.username == "test"
    assert user.email == "test@example.com"

    users = service.get_users()
    assert len(users) == 1


def test_duplicate_email():
    repo = UserRepository()
    service = UserService(repo)
    service.register_user("test1", "test@example.com")
    try:
        service.register_user("test2", "test@example.com")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Email already registered"


def test_api_endpoints():
    client = TestClient(app)
    # FastAPI handles query params or JSON body. The current route uses query params
    # due to how create_user is defined with username: str, email: str (no Body or Depends/Schema)
    response = client.post("/users/?username=alice&email=alice@example.com")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"

    response = client.get("/users/")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 1
    assert users[0]["email"] == "alice@example.com"


def test_api_duplicate_email():
    client = TestClient(app)
    client.post("/users/?username=alice&email=alice@example.com")
    response = client.post("/users/?username=alice2&email=alice@example.com")
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"
