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
from services.users.endpoints import HOST

class GamesAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()
        self.Update_payloads = UpdatePayloads()

    @allure.step("List all games")
    def list_all_games(self):
        response = requests.get(
            url=self.endpoints.list_all_games,
            headers=self.headers.basic_api_2,
            params={"offset": 0, "limit": 10}
        )
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"
        response_json = response.json()
        print("Response JSON:", response_json)
        self.attach_response(response_json)
        return response_json

    @allure.step("Search games")
    def search_games(self):
        params = {
            "query": "The Witcher 3",
            "offset": 0,
            "limit": 10
        }
        response = requests.get(
            url=self.endpoints.search_games,
            headers=self.headers.basic_api_2,
            params=params
        )
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}, Response: {response.text}"
        response_json = response.json()
        self.attach_response(response_json)
        # Проверяем только на ключевые поля
        games = response_json.get("games", [])
        assert len(games) > 0, "No games found in the response"
        game = games[0]
        assert game["title"] == "The Witcher 3: Wild Hunt", f"Unexpected title: {game['title']}"
        assert game["price"] == 999, f"Unexpected price: {game['price']}"

    @allure.step("Get game by UUID: {game_uuid}")
    def get_game_by_uuid(self, game_uuid):
        url = f"{HOST}/games/{game_uuid}"
        response = requests.get(
            url=url,
            headers=self.headers.basic_api_9  # Используем необходимые заголовки
        )
        assert response.status_code == 200, (
            f"Unexpected status code: {response.status_code}, Response: {response.text}"
        )
        response_json = response.json()
        print(f"Response JSON from get_game_by_uuid: {response_json}")
        self.attach_response(response_json)
        return response_json

