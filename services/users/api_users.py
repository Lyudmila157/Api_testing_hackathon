import allure
import requests

from utils.helper import Helper
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers
from services.users.models.user_model import UserModel
from services.users.params import Params
from services.users.Update_payloads import UpdatePayloads
from requests.exceptions import JSONDecodeError


class UsersAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()
        self.Update_payloads = UpdatePayloads()

    @allure.step("Create user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_api_3,
            json=self.payloads.create_user
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Get user by ID")
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic_api_23,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("List_all_users")
    def list_all_users(self):
        response = requests.get(
            url=self.endpoints.list_all_user,
            headers=self.headers.basic_api_21,
            params={"offset": 10}
        )
        self.attach_response(response.json())
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        # response_json = response.json()
        # print("Full response:", response_json)
        # assert "offset" in response_json, f"Key 'offset' not found in response: {response_json}"
        # assert response_json["offset"] == 10

    @allure.step("Delete user")
    def delete_user(self, user_uuid):
        url = self.endpoints.delete_a_user(user_uuid)
        response = requests.delete(
            url=url,
            headers=self.headers.basic_api_1
        )

        print(f"Response status code: {response.status_code}")

        # Если тело ответа пустое
        if response.status_code == 204:
            print(f"User with UUID {user_uuid} deleted successfully.")
            self.attach_response({"status_code": response.status_code, "message": "User deleted successfully"})
            return
        else:
            # Если тело не пустое, пытаемся обработать JSON
            try:
                response_json = response.json()
            except requests.exceptions.JSONDecodeError:
                response_json = {"error": "Response is not a valid JSON", "raw_response": response.text}

            print(f"Response body: {response_json}")
            assert response.status_code == 204, f"Failed to delete user. Status code: {response.status_code}, Response: {response_json}"

        self.attach_response(response.json())
        if response.status_code == 204:
            print(f"User with UUID {user_uuid} deleted successfully.")
        else:
            print(f"Failed to delete user. Status code: {response.status_code}, Response: {response.text}")

    @allure.step("Get user")
    def get_user(self):
        response = requests.get(
            url=self.endpoints.get_user,
            headers=self.headers.basic_api_23
        )
        self.attach_response(response.json())
        if response.status_code == 200:
            users = response.json().get("users", [])
            if users:
                user_uuid = users[0]["uuid"]
                print(f"User UUID: {user_uuid}")
                return user_uuid
            else:
                print("No users found")
        else:
            print(f"Failed to fetch users. Status code: {response.status_code}")

    @allure.step("Update user")
    def update_user(self, user_uuid, user_data):
        response = requests.patch(
            url=self.endpoints.update_a_user(user_uuid),
            json=user_data,
            headers=self.headers.basic_api_24
        )
        self.attach_response(response.json())
        if response.status_code == 200:
            print(f"User with UUID {user_uuid} updated successfully.")
        else:
            print(f"Failed to update user. Status code: {response.status_code}")

    # @allure.step("Delete_2")
    # def delete_2(self):
    #     response = requests.get(
    #         url=self.endpoints.list_all_user,
    #         headers=self.headers.basic_api_21
    #     )
    #     users = response.json().get("users", [])
    #     user_uuids = [user["uuid"] for user in users]
    #     assert user_uuid not in user_uuids, f"Deleted user UUID {user_uuid} still exists in user list."

    @allure.step("Check if user is deleted")
    def is_user_deleted(self, user_uuid):
        response = requests.get(
            url=self.endpoints.list_all_user,
            headers=self.headers.basic_api_21
        )
        self.attach_response(response.json())
        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch user list. Status code: {response.status_code}, Response: {response.text}")

        users = response.json().get("users", [])
        user_uuids = [user["uuid"] for user in users]

        return user_uuid not in user_uuids

    @allure.step("Get a user by email and password")
    def get_a_user_by_email_and_password(self):
        response = requests.post(
            url=self.endpoints.get_a_user_by_email_and_password,
            headers=self.headers.basic_api_7,
            json=self.payloads.get_a_user_by_email_and_password
        )
        self.attach_response(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())

