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
from config.headers import Headers
from services.users.endpoints import HOST


class CartAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.params = Params()
        self.Update_payloads = UpdatePayloads()

    @allure.step("Get a cart by user uuid ")
    def get_a_cart(self, user_uuid):
        url = self.endpoints.get_a_cart(user_uuid)
        response = requests.get(
            url=url,
            headers=self.headers.basic_api_12
        )
        self.attach_response(response.json())
        if response.status_code == 200:
            print(f"Successfully retrieved cart for user {user_uuid}")
            return response.json()
        else:
            print(f"Failed to retrieve user cart. Status code: {response.status_code}, Response: {response.text}")
            return None

    @allure.step("Add an item to user's cart")
    def add_an_item_to_users_cart(self, user_uuid, item_uuid, quantity):
        url = self.endpoints.add_an_item_to_users_cart(user_uuid)
        payload = {
            "item_uuid": item_uuid,
            "quantity": quantity
        }
        response = requests.post(
            url=url,
            headers=self.headers.basic_api_13,
            json=payload
        )
        self.attach_response(response.json())
        if response.status_code == 200:
            print(f"The user's cart with UUID {user_uuid} was updated successfully")
            print(f"Response: {response.json()}")
        else:
            print(f"Failed to update user's cart. Status code: {response.status_code}, Response: {response.text}")

    @allure.step("Change an item from users cart")
    def change_an_item_from_users_cart(self, user_uuid, item_uuid, new_quantity):
        # текущие данные корзины пользователя
        cart_data = self.get_a_cart(user_uuid)
        # Проверь, есть ли товар в корзине
        item_in_cart = next((item for item in cart_data.get("items", []) if item["item_uuid"] == item_uuid), None)
        if item_in_cart:
            # Обнови количество существующего товара в корзине
            item_in_cart["quantity"] = new_quantity
            payload = {
                "item_uuid": item_uuid,
                "quantity": new_quantity
            }
            url = self.endpoints.add_an_item_to_users_cart(
                user_uuid)
            response = requests.post(
                url=url,
                headers=self.headers.basic_api_13,
                json=payload
            )
            self.attach_response(response.json())
            if response.status_code == 200:
                print(f"Quantity for item {item_uuid} updated successfully in cart of user {user_uuid}.")
                print(f"Response: {response.json()}")
            else:
                print(f"Failed to update item quantity. Status code: {response.status_code}, Response: {response.text}")
        else:
            print(f"Item {item_uuid} not found in cart of user {user_uuid}.")

    @allure.step("Removes an item from user's cart")
    def remove_an_item_from_users_cart(self, user_uuid: str, item_uuid: str, new_quantity: int):
        # текущие данные корзины
        cart_data = self.get_a_cart(user_uuid)
        print(f"Current Cart Data: {cart_data}")
        # Проверь, есть ли товар в корзине
        item_in_cart = next((item for item in cart_data.get("items", []) if item["item_uuid"] == item_uuid), None)
        if not item_in_cart:
            print(f"Item {item_uuid} not found in cart for user {user_uuid}.")
            return None  # Возвратим None, чтобы указать на отсутствие товара

        payload = {
            "item_uuid": item_uuid,
            "quantity": new_quantity
        }
        url = self.endpoints.remove_an_item_in_user_cart(user_uuid)
        response = requests.post(
            url=url,
            headers=self.headers.basic_api_13,
            json=payload
        )
        if response.status_code == 200:
            print(f"Quantity for item {item_uuid} updated successfully in cart of user {user_uuid}.")
            print(f"Response: {response.json()}")
        else:
            print(f"Failed to update item quantity. Status code: {response.status_code}, Response: {response.text}")
        self.attach_response(response.json())
        return response

    @allure.step("Clear user's cart")
    def clear_users_cart(self, user_uuid):
        url = self.endpoints.clear_user_cart(user_uuid)
        payload = {
            "items": [],
            "total_price": 0,
            "user_uuid": user_uuid
        }
        response = requests.post(
            url=url,
            headers=self.headers.basic_api_15,
            json=payload
        )
        self.attach_response(response.json())
        if response.status_code == 200:
            print(f"Cart for user {user_uuid} cleared successfully.")
            print(f"Response: {response.json()}")
        else:
            print(
                f"Failed to clear cart for user {user_uuid}. Status code: {response.status_code}, Response: {response.text}")
        return response