import allure
import requests

from utils.helper import Helper
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers


class AvatarsAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Update user's avatar")
    def update_user_avatar(self, user_uuid, avatar_data):

        url = self.endpoints.update_avatar(user_uuid)
        print(f"Request URL: {url}")

        payload = {"avatar": avatar_data}
        print(f"Payload: {payload}")

        response = requests.put(
            url=url,
            headers=self.headers.basic_api_11,
            json=payload
        )

        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.json()}")

        assert response.status_code == 200, f"Failed to update avatar. Status code: {response.status_code}, Response: {response.json()}"
        self.attach_response(response.json())
        return response.json()
