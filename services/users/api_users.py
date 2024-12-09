import allure
import requests

from utils.helper import Helper
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers
from services.users.models.user_model import UserModel
from services.users.params import Params
from services.users.Update_payloads import UpdatePayloads
from conftest import generate_unique_user_data
import uuid


class UsersAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()
        self.Update_payloads = UpdatePayloads()

    @allure.step("Create user and uuid with model unique")
    def create_user_and_uuid_with_model_unique(self):
        user_data = generate_unique_user_data()
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_api_3,
            json=user_data
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Create user with params on test email and password")
    def create_user_with_params_on_test_email_and_password(self):
        unique_id = str(uuid.uuid4())
        user_data = {
            "email": f"max_{unique_id}@example.org",
            "password": "password",
            "name": "Max",
            "nickname": f"max_{unique_id}"
        }
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_api_3,
            json=user_data
        )
        assert response.status_code == 200, f"Failed to create user: {response.text}"
        self.attach_response(response.json())
        return {**user_data, **response.json()}

    @allure.step("Create user and uuid with model")
    def create_user_and_uuid_with_model(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_api_3,
            json=self.payloads.create_user
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Create user with params")
    def create_user_with_params(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic_api_3,
            json=self.payloads.create_a_new_user_with_params
        )
        assert response.status_code == 200, "error"
        self.attach_response(response.json())
        return response.json()

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
            params={"offset": 0, "limit": 10}
        )
        try:
            json_response = response.json()
        except ValueError:
            print(f"Failed to parse JSON response: {response.text}")
            raise ValueError("Response is not in JSON format")
        self.attach_response(json_response)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"
        print(f"Response JSON: {json_response}")
        return json_response

    @allure.step("Delete user")
    def delete_user(self, user_uuid: str):
        url = self.endpoints.delete_a_user(user_uuid)
        response = requests.delete(
            url=url,
            headers=self.headers.basic_api_1
        )
        print(f"Request URL: {url}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        if response.status_code == 204:
            print(f"User with UUID {user_uuid} deleted successfully.")
            self.attach_response({"status_code": response.status_code, "message": "User deleted successfully"})
            return {"status_code": response.status_code, "message": "User deleted successfully"}
        try:
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            response_json = {"error": "Response is not a valid JSON", "raw_response": response.text}

        print(f"Response Body: {response_json}")
        assert response.status_code == 204, f"Failed to delete user. Status code: {response.status_code}, Response: {response_json}"

    @allure.step("Get a user")
    def get_a_user(self, user_uuid: str):
        url = self.endpoints.get_user(user_uuid)
        print(f"Request URL: {url}")
        response = requests.get(
            url=url,
            headers=self.headers.basic_api_23
        )
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        self.attach_response(response.json())
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        return response.json()

    @allure.step("Update user")
    def update_user(self, user_uuid, user_data):
        url = self.endpoints.update_a_user(user_uuid)
        print(f"Request URL: {url}")
        print(f"Request Payload: {user_data}")
        response = requests.patch(
            url=url,
            json=user_data,
            headers=self.headers.basic_api_24
        )
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        self.attach_response(response.json())
        assert response.status_code == 200, (
            f"Failed to update user. Status code: {response.status_code}, Response: {response.text}"
        )
        print(f"User with UUID {user_uuid} updated successfully.")
        return response.json()

    @allure.step("Get a user by email and password")
    def get_a_user_by_email_and_password_old(self):
        payload = self.payloads.get_a_user_by_email_and_password
        response = requests.post(
            url=self.endpoints.get_a_user_by_email_and_password,
            headers=self.headers.basic_api_7,
            json=payload
        )
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        self.attach_response(response.json())
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"
        response_data = response.json()
        assert response_data["email"] == payload["email"], "Email in response does not match the requested email"
        return response_data

    @allure.step("Get a user by email and password")
    def get_a_user_by_email_and_password_new(self, email, password):
        payload = {"email": email, "password": password}
        response = requests.post(
            url=self.endpoints.get_a_user_by_email_and_password,
            headers=self.headers.basic_api_7,
            json=payload
        )
        assert response.status_code == 200, f"Failed to get user: {response.text}"
        self.attach_response(response.json())
        return response.json()
