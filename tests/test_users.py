import json
import allure
import pytest

from config.base_test import BaseTest
from services.users.Update_payloads import UpdatePayloads


@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @pytest.mark.users
    @allure.title("Create new user and uuid")
    def test_create_user_and_uuid_with_model(self):
        user = self.api_users.create_user_and_uuid_with_model()
        self.api_users.get_user_by_id(user.uuid)

    # @pytest.mark.users
    # @allure.title("Create new user")
    # def test_create_user_with_params(self):
    #     user_data = self.api_users.create_user_with_params()
    #     print(user_data)

    @pytest.mark.users
    @allure.title("Get user by id")
    def test_get_user_by_id(self):
        user = self.api_users.create_user_and_uuid_with_model_unique()
        self.api_users.get_user_by_id(user.uuid)

    @pytest.mark.users
    @allure.title("List all users")
    def test_list_all_users(self):
        response_data = self.api_users.list_all_users()
        assert response_data is not None, "Response is None"
        assert isinstance(response_data, dict), "Response is not a valid JSON object"
        status_code = 200
        print(f"Status Code: {status_code}")
        assert "meta" in response_data, "Response does not contain 'meta' key"
        assert "total" in response_data["meta"], "'meta' does not contain 'total'"
        assert "users" in response_data, "Response does not contain 'users' key"
        assert len(response_data["users"]) > 0, "No users found in the response"
        print(f"Response JSON: {response_data}")

    @pytest.mark.users
    @allure.title("Delete a user by UUID")
    def test_delete_user(self):
        created_user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = created_user.uuid
        assert user_uuid, "Failed to create user. UUID is empty."
        delete_response = self.api_users.delete_user(user_uuid)
        assert delete_response["status_code"] == 204, "User was not deleted successfully."
        with pytest.raises(Exception, match="404"):
            self.api_users.get_a_user(user_uuid)


    @pytest.mark.users
    @allure.title("Create and get a user")
    def test_create_and_get_a_user(self):
        new_user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = new_user.uuid
        user_data = self.api_users.get_a_user(user_uuid)
        print(f"Retrieved User Data: {user_data}")
        assert user_data["uuid"] == user_uuid, "UUID mismatch"
        assert "email" in user_data, "Email is missing"

    @pytest.mark.users
    @allure.title("Update user")
    def test_update_user(self):
        user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = user.uuid
        assert user_uuid, "User UUID should not be None or empty"
        user_data = UpdatePayloads.update_user
        updated_user = self.api_users.update_user(user_uuid, user_data)
        assert updated_user["name"] == user_data["name"], "Name was not updated correctly"
        assert updated_user["nickname"] == user_data["nickname"], "Nickname was not updated correctly"
        assert updated_user["email"] == user_data["email"], "Email was not updated correctly"

    @pytest.mark.users
    @allure.title("Get a user by email and password")
    def test_get_a_user_by_email_and_password(self):
        created_user = self.api_users.create_user_with_params_on_test_email_and_password()
        retrieved_user = self.api_users.get_a_user_by_email_and_password_new(
            email=created_user["email"],
            password=created_user["password"]
        )
        assert retrieved_user["email"] == created_user["email"], "Email does not match"
        assert retrieved_user["name"] == created_user["name"], "Name does not match"
        assert retrieved_user["nickname"] == created_user["nickname"], "Nickname does not match"
        assert retrieved_user["uuid"] == created_user["uuid"], "UUID does not match"

        print("User retrieved successfully:", retrieved_user)

        # created_user = self.api_users.create_user_with_params()
        # retrieved_user = self.api_users.get_a_user_by_email_and_password()
        # assert retrieved_user["email"] == created_user["email"], "Email does not match"
        # assert retrieved_user["name"] == created_user["name"], "Name does not match"
        # assert retrieved_user["nickname"] == created_user["nickname"], "Nickname does not match"
        # assert retrieved_user["avatar_url"] == created_user["avatar_url"], "Avatar URL does not match"
        # assert retrieved_user["uuid"] == created_user["uuid"], "UUID does not match"
        # print("User retrieved successfully:", retrieved_user)


    # @pytest.mark.users
    # @allure.title("Delete a user by UUID")
    # def test_delete_user_new(self):
    #     created_user = self.api_users.create_user_with_params()
    #     user_uuid = created_user["uuid"]
    #     assert user_uuid, "Failed to create user. UUID is empty."
    #     delete_response = self.api_users.delete_user(user_uuid)
    #     assert delete_response["status_code"] == 204, "User was not deleted successfully."
    #     with pytest.raises(Exception, match="404"):
    #         self.api_users.get_a_user(user_uuid)