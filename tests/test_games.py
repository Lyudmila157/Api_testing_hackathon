import json
import allure
import pytest

from config.base_test import BaseTest
from services.users.Update_payloads import UpdatePayloads


@allure.epic("Games Tests")
@allure.feature("Games")
class TestGames(BaseTest):

    @pytest.mark.categories
    @allure.title("List all games")
    def test_list_all_games(self):
        response_json = self.api_games.list_all_games()
        assert "games" in response_json, f"'games' not found in the response: {response_json}"

    @pytest.mark.games
    @allure.title("Search games")
    def test_search_games(self):
        self.api_games.search_games()

    @pytest.mark.games
    @allure.title("Get game by UUID")
    def test_get_game_by_uuid(self):
        response_json = self.api_games.list_all_games()
        assert "games" in response_json, f"'games' not found in the response: {response_json}"
        first_game = response_json["games"][0]
        first_game_uuid = first_game["uuid"]
        assert first_game_uuid, "No UUID found in the list of games"
        game_details = self.api_games.get_game_by_uuid(first_game_uuid)
        assert game_details == first_game, (
            f"Game details mismatch. Expected: {first_game}, Got: {game_details}"
        )
