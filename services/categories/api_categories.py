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
from conftest import HOST

class CategoriesAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()
        self.Update_payloads = UpdatePayloads()

    @allure.step("List all categories")
    def list_all_categories(self):
        response = requests.get(
            url=self.endpoints.list_all_categories,
            headers=self.headers.basic_api_10,
            params={"offset": 0, "limit": 10}
        )
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"
        response_json = response.json()
        print("Response JSON:", response_json)
        self.attach_response(response_json)
        return response_json

    @allure.step("Get games by category: {category_uuid}")
    def get_games_by_category(self, category_uuid):
        url = f"{HOST}/categories/{category_uuid}/games"
        params = {
            "offset": 0,
            "limit": 10
        }
        response = requests.get(url, headers=self.headers.basic_api_2, params=params)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"
        response_json = response.json()
        self.attach_response(response_json)
        assert "games" in response_json, f"Key 'games' is missing in the response: {response_json}"
        return response_json["games"]

    @allure.step("Get games by category: {category_uuid} new")
    def get_games_by_category_new(self, category_uuid):
        url = f"{HOST}/categories/{category_uuid}/games"
        params = {
            "offset": 0,
            "limit": 10
        }
        response = requests.get(url, headers=self.headers.basic_api_2, params=params)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"
        response_json = response.json()
        self.attach_response(response_json)
        if "games" in response_json and isinstance(response_json["games"], list) and len(response_json["games"]) > 0:
            single_game = response_json["games"][0]
            print(f"Single game selected: {single_game}")
            return single_game
        else:
            assert False, "No games found or 'games' key is missing in the response."

