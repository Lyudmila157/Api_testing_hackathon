import allure
import pytest
import requests

from config.base_test import BaseTest
from services.users.Update_payloads import UpdatePayloads


@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @pytest.mark.users
    @allure.title("Create new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        self.api_users.get_user_by_id(user.uuid)

    @pytest.mark.users
    @allure.title("List all users")
    def test_list_all_users(self):
        self.api_users.list_all_users()

    @pytest.mark.users
    @allure.title("Delete user")
    def test_delete_user(self):
        user_uuid = self.api_users.get_user()
        if user_uuid:
            self.api_users.delete_user(user_uuid)
        else:
            pytest.fail("User UUID not found. Cannot perform deletion.")

    @pytest.mark.users
    @allure.title("Get user")
    def test_get_user(self):
        self.api_users.get_user()

    @pytest.mark.users
    @allure.title("Update user")
    def test_update_user(self):
        user_uuid = self.api_users.get_user()
        if user_uuid:
            user_data = UpdatePayloads.update_user
            self.api_users.update_user(user_uuid, user_data)
        else:
            pytest.fail("User UUID not found. Cannot perform update.")

    @pytest.mark.users
    @allure.title("Delete user and verify user not in list")
    def test_delete_user_and_verify(self):
        user_uuid = self.api_users.get_user()

        if user_uuid:
            self.api_users.delete_user(user_uuid)

            is_deleted = self.api_users.is_user_deleted(user_uuid)
            assert is_deleted, f"Deleted user UUID {user_uuid} still exists in user list."
        else:
            pytest.fail("User UUID not found. Cannot perform deletion.")

    @pytest.mark.users
    @allure.title("Get a user by email and password")
    def test_get_a_user_by_email_and_password(self):
        self.api_users.get_a_user_by_email_and_password()