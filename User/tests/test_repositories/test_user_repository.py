from datetime import datetime
from User.models.user_model import UserMain, user_client
import asyncio

def test_user_repository():
    user = UserMain(
        id=1,
        name="Emmanuel",
        username="Alejo1505@",
        email="alejo15@hotmal.com",
        hashed_password="manuelRam15",
    )
    
    assert user.id == 1
    assert user.name == "Emmanuel"
    assert user.username == "Alejo1505@"
    assert user.email == "alejo15@hotmal.com"
    assert user.hashed_password == "manuelRam15"
    assert isinstance(user.created_at, datetime)
    assert user.update is None

def test_user_repository1():
    user = UserMain(
        id=1,
        name="Emmanuel",
        username="Alejo1505@",
        email="alejo15@hotmal.com",
        hashed_password="manuelRam15",
    )
    result = asyncio.run(user_client(user))
    assert result.id == 1
    assert result.name == "Emmanuel"
    assert result.username == "Alejo1505@"
    assert result.email == "alejo15@hotmal.com"
    assert result.hashed_password == "manuelRam15"
