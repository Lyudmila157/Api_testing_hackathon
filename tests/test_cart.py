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
    @allure.title("Change an item to user cart")
    def test_change_an_item_to_user_cart(self):
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
        self.api_cart.change_an_item_from_users_cart(user_uuid, item_uuid, new_quantity)
        # Проверяем, что количество изменилось
        updated_cart_data = self.api_cart.get_a_cart(user_uuid)
        updated_item = next((item for item in updated_cart_data["items"] if item["item_uuid"] == item_uuid), None)
        assert updated_item is not None, f"Item {item_uuid} not found in updated cart"
        assert updated_item[
                   "quantity"] == new_quantity, f"Expected quantity {new_quantity}, but got {updated_item['quantity']}"

    @pytest.mark.cart
    @allure.title("Remove an item from user's cart")
    def test_remove_an_item_from_user_cart(self):
        new_user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = new_user.uuid
        user_data = self.api_users.get_a_user(user_uuid)
        print(f"Retrieved User Data: {user_data}")
        assert user_data["uuid"] == user_uuid, "UUID mismatch"
        assert "email" in user_data, "Email is missing"
        # Проверь состояние корзины
        cart_data = self.api_cart.get_a_cart(user_uuid)
        assert cart_data is not None, "Failed to retrieve user's cart"
        print(f"Initial Cart Data: {cart_data}")
        # список доступных игр
        games_list = self.api_games.list_all_games()
        assert games_list.get("games"), "No games available in the list"
        item_uuid = games_list["games"][0]["uuid"]
        print(f"Selected Game UUID: {item_uuid}")
        # Добавь товар в корзину, если она пуста
        if not cart_data.get("items"):
            print("Cart is empty. Adding a new item.")
            self.api_cart.add_an_item_to_users_cart(user_uuid, item_uuid, 1)
            cart_data = self.api_cart.get_a_cart(user_uuid)
            print(f"Updated Cart Data After Adding: {cart_data}")
        # Проверь, что элемент добавлен
        item_in_cart = next((item for item in cart_data.get("items", []) if item["item_uuid"] == item_uuid), None)
        assert item_in_cart, f"Item {item_uuid} was not added to the cart"
        # Удаляем товар из корзины
        print(f"Removing item {item_uuid} from cart...")
        remove_response = self.api_cart.remove_an_item_from_users_cart(user_uuid, item_uuid, 0)
        assert remove_response.status_code == 200, f"Failed to remove item from cart. Status code: {remove_response.status_code}"
        # Проверь, что элемент удален
        updated_cart_data = self.api_cart.get_a_cart(user_uuid)
        print(f"Updated Cart Data After Removing: {updated_cart_data}")
        removed_item = next((item for item in updated_cart_data.get("items", []) if item["item_uuid"] == item_uuid),
                            None)
        assert removed_item is None, f"Item {item_uuid} was not removed from the cart"

        print(f"Item {item_uuid} successfully removed from cart of user {user_uuid}.")

    @pytest.mark.cart
    @allure.title("Clear user's cart")
    def test_clear_users_cart(self):
        new_user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = new_user.uuid
        user_data = self.api_users.get_a_user(user_uuid)
        print(f"Retrieved User Data: {user_data}")
        assert user_data["uuid"] == user_uuid, "UUID mismatch"
        assert "email" in user_data, "Email is missing"
        # Добавить товары в корзину
        games_list = self.api_games.list_all_games()
        assert games_list.get("games"), "No games available in the list"
        item_uuid = games_list["games"][0]["uuid"]
        print(f"Selected Game UUID: {item_uuid}")
        self.api_cart.add_an_item_to_users_cart(user_uuid, item_uuid, 1)
        # проверяем, что товар добавлен
        cart_data = self.api_cart.get_a_cart(user_uuid)
        assert cart_data["items"], "Cart is empty, but it should contain items."
        clear_response = self.api_cart.clear_users_cart(user_uuid)
        assert clear_response.status_code == 200, f"Failed to clear cart. Status code: {clear_response.status_code}"
        # проверим, что корзина пуста
        updated_cart_data = self.api_cart.get_a_cart(user_uuid)
        assert updated_cart_data["items"] == [], "Cart is not empty after clearing."
        assert updated_cart_data["total_price"] == 0, "Total price is not zero after clearing."
        print(f"Cart successfully cleared for user {user_uuid}.")