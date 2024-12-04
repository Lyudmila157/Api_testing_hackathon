import allure
import pytest
import requests


from config.base_test import BaseTest
from services.users.Update_payloads import UpdatePayloads
import os

@allure.epic("Users Avatars")
@allure.feature("Avatars")
class TestAvatars(BaseTest):
    @pytest.mark.avatar
    @allure.title("Update user's avatar")
    def test_update_user_avatar(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Каталог текущего файла (теста)
        avatar_data = os.path.join(base_dir, "..", "services", "users", "avatar_file", "cat.jpg")
        avatar_data = os.path.abspath(avatar_data)  # Преобразуем в абсолютный путь

        # Проверяем существование файла
        if not os.path.exists(avatar_data):
            raise FileNotFoundError(f"Avatar file not found: {avatar_data}")

        user_uuid = self.api_users.get_user()
        assert user_uuid, "Failed to retrieve user UUID"
        print(f"User UUID: {user_uuid}")
        print(f"Avatar data: {avatar_data}")

        try:
            # Обновление аватара
            response = self.avatars_api.update_user_avatar(user_uuid, avatar_data)

            # Проверяем, что в ответе есть 'avatar_url', что подтверждает успешное обновление
            assert "avatar_url" in response, f"Avatar update failed. Response: {response}"
            print(f"Avatar updated successfully for user {user_uuid}. Avatar URL: {response['avatar_url']}")

        except Exception as e:
            print(f"Test failed with error: {e}")
            assert False, f"Test failed with error: {e}"
