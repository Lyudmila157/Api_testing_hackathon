import json
import allure
import pytest

from config.base_test import BaseTest
from services.users.Update_payloads import UpdatePayloads


@allure.epic("Cart tests")
@allure.feature("Cart")
class TestCart(BaseTest):

    @pytest.mark.cart
    @allure.title("Get a cart")
    def test_get_a_cart(self):
        new_user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = new_user.uuid
        user_data = self.api_users.get_a_user(user_uuid)
        print(f"Retrieved User Data: {user_data}")
        assert user_data["uuid"] == user_uuid, "UUID mismatch"
        assert "email" in user_data, "Email is missing"
        wishlist_data = self.api_cart.get_a_cart(user_uuid)
        assert wishlist_data is not None, "Failed to retrieve users cart"
        assert len(wishlist_data.get("items", [])) >= 0, "User cart is empty or failed"

    @pytest.mark.cart
    @allure.title("Add an item to user's cart")
    def test_add_an_item_to_users_cart(self):
        new_user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = new_user.uuid
        user_data = self.api_users.get_a_user(user_uuid)
        print(f"Retrieved User Data: {user_data}")
        assert user_data["uuid"] == user_uuid, "UUID mismatch"
        assert "email" in user_data, "Email is missing"
        # данные о корзине пользователя
        wishlist_data = self.api_cart.get_a_cart(user_uuid)
        assert wishlist_data is not None, "Failed to retrieve user's cart"
        # список всех доступных игр
        games_data = self.api_games.list_all_games()
        assert "games" in games_data, "'games' not found in the response"

        game = games_data["games"][0]
        item_uuid = game["uuid"]
        print(f"Selected Game UUID: {item_uuid}")

        # Данные о корзине
        cart_items = wishlist_data.get("items", [])
        quantity = 1

        # Если корзина не пуста, проверить нужно наличие этого товара
        if cart_items:
            existing_item = next((item for item in cart_items if item["item_uuid"] == item_uuid), None)
            if existing_item:
                print(f"Item {item_uuid} is already in the cart. Updating quantity to {quantity}.")
                quantity += existing_item["quantity"]
        else:
            print("Cart is empty. Adding a new item.")

        assert quantity <= 100, "Quantity exceeds the allowed limit (100)."

        self.api_cart.add_an_item_to_users_cart(user_uuid, item_uuid, quantity)

    @pytest.mark.cart
    @allure.title("Change quantity for already existing item in user's cart")
    def test_change_quantity_for_existing_item_in_users_cart(self):
        new_user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = new_user.uuid
        user_data = self.api_users.get_a_user(user_uuid)
        print(f"Retrieved User Data: {user_data}")
        assert user_data["uuid"] == user_uuid, "UUID mismatch"
        assert "email" in user_data, "Email is missing"
        wishlist_data = self.api_cart.get_a_cart(user_uuid)
        assert wishlist_data is not None, "Failed to retrieve user's cart"
        games_list = self.api_games.list_all_games()  # Получаем список всех игр
        assert games_list.get("games"), "No games available in the list"
        item_uuid = games_list["games"][0]["uuid"]
        print(f"Selected Game UUID: {item_uuid}")
        # Если корзина пуста, добавь товар
        cart_items = self.wishlist_users.add_an_item_to_users_wishlist("items", [])
        if not cart_items:
            print("Cart is empty. Adding a new item.")
            self.api_cart.add_an_item_to_users_cart(user_uuid, item_uuid, 1)

        new_quantity = 2
        assert new_quantity <= 100, "Quantity exceeds the allowed limit (100)."
        # Меняем количество товара в корзине
        self.api_cart.change_quantity_for_existing_item_in_cart(user_uuid, item_uuid, new_quantity)
        # Проверяем, что количество изменилось
        updated_cart_data = self.api_cart.get_a_cart(user_uuid)
        updated_item = next((item for item in updated_cart_data["items"] if item["item_uuid"] == item_uuid), None)
        assert updated_item is not None, f"Item {item_uuid} not found in updated cart"
        assert updated_item[
                   "quantity"] == new_quantity, f"Expected quantity {new_quantity}, but got {updated_item['quantity']}"
