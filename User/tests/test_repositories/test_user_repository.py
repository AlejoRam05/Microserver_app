from datetime import datetime
from User.models.user_model import UserMain, user_client
import asyncio

def test_user_repository():
    user_data = {
        "id": 1,
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "hashed_password": "hashed_pass_123"
    }
    user = UserMain(**user_data)
    
    assert user.id == 1
    assert user.name == "John Doe"
    assert user.username == "johndoe"
    assert user.email == "johndoe@example.com"
    assert user.hashed_password == "hashed_pass_123"
    assert isinstance(user.created_at, datetime)
    assert user.updated_at is None

def test_user_repository1():
    user_data = {
        "id": 1,
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "hashed_password": "hashed_pass_123"
    }
    user = UserMain(**user_data)
    result = asyncio.run(user_client(user))
    assert result == user
