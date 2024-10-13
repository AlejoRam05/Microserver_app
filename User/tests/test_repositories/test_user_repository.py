from datetime import datetime
from User.models.user_model import UserMain


def test_user_repository():
    user_data = {
        "id": int,
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "hashed_password": "hashed_pass_123"
    }
    user = UserMain(**user_data)
    
    assert user.id is int
    assert user.name == "John Doe"
    assert user.username == "johndoe"
    assert user.email == "johndoe@example.com"
    assert user.hashed_password == "hashed_pass_123"
    assert isinstance(user.created_at, datetime)
    assert user.updated_at is None


