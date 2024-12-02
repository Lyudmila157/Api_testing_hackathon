import allure
import pytest
import requests

from config.base_test import BaseTest
from services.users.Update_payloads import UpdatePayloads


@allure.epic("Users Avatars")
@allure.feature("Avatars")
class TestAvatars(BaseTest):

    @pytest.mark.avatar
    @allure.title("Update user's avatar")
    def test_update_user_avatar(self):
        user_uuid = self.api_users.get_user()
        assert user_uuid, "Failed to retrieve user UUID"
        print(f"User UUID: {user_uuid}")
        avatar_data = "users/avatar_file/cat.jpg"
        print(f"Avatar data: {avatar_data}")
        response = self.avatars_api.update_user_avatar(user_uuid, avatar_data)
        assert response.get("success") is True, f"Avatar update failed. Response: {response}"
        print(f"Avatar updated successfully for user {user_uuid}")
