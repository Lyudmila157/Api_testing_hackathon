import os
from dotenv import load_dotenv
import requests
import pytest
import uuid

load_dotenv()

HOST = "https://release-gs.qa-playground.com/api/v1"
# HOST = "https://dev-gs.qa-playground.com/api/v1"
# HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" else "https://release-gs.qa-playground.com/api/v1"


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response = requests.post(
        url=f"{HOST}/setup",
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
    )
    assert response.status_code == 205

def generate_unique_user_data():
    unique_id = str(uuid.uuid4())
    return {
        "email": f"user_{unique_id}@example.org",
        "name": f"TestUser_{unique_id}",
        "nickname": f"Nick_{unique_id}",
        "avatar_url": f"https://avatar.com/{unique_id}",
        "password": f"Password_{unique_id}"  # Добавляем уникальный пароль
    }

# @pytest.fixture(autouse=True, scope="function")
# def cleanup_users(api_users):
#     """
#     Глобальная фикстура для очистки пользователей после каждого теста.
#     """
#     yield
#     api_users.cleanup_all_users()  # Реализуйте метод для массовой очистки


