import json
import allure
import pytest

from config.base_test import BaseTest
from services.users.Update_payloads import UpdatePayloads


@allure.epic("Categories tests")
@allure.feature("Categories")
class TestCategories(BaseTest):

    @pytest.mark.categories
    @allure.title("List all categories")
    def test_list_all_categories(self):
        response_json = self.api_categories.list_all_categories()
        assert "categories" in response_json, f"'categories' not found in the response: {response_json}"

    @pytest.mark.categories
    @allure.title("Get games by category")
    def test_get_games_by_category(self):
        category_uuid = '8126d35b-5336-41ad-981d-f245c3e05665'
        games = self.api_categories.get_games_by_category(category_uuid)
        assert len(games) > 0, "No games found in this category"

    @pytest.mark.categories
    @allure.title("Get games by category dinamic")
    def test_get_games_by_category_dinamic(self):
        response_json = self.api_categories.list_all_categories()
        category_uuid = response_json['categories'][1]['uuid']
        self.api_categories.get_games_by_category(category_uuid)

    @pytest.mark.categories
    @allure.title("Get games by category dynamic new")
    def test_get_games_by_category_dynamic_new(self):
        response_json = self.api_categories.list_all_categories()
        category_uuid = response_json['categories'][1]['uuid']
        game = self.api_categories.get_games_by_category_new(category_uuid)
        assert game is not None, "No games found for the selected category."
        assert "title" in game, f"Game does not have 'title': {game}"
