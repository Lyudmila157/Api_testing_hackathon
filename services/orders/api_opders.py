import allure
import requests

from utils.helper import Helper
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers



class OrdersAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create a new order")
    def create_a_new_order(self, user_uuid):
        url = self.endpoints.get_user_wishlist(user_uuid)
        response = requests.post(
            url=url,
            headers=self.headers.basic_api_16,
            json=self.payloads.create_a_new_order
        )
        self.attach_response(response.json())
        if response.status_code == 204:
            print(f"User with UUID {user_uuid} successfully.")
        else:
            print(f"Failed Status code: {response.status_code}, Response: {response.text}")

        self.attach_response(response.json())
        if response.status_code == 200:
            print(f"The orders with UUID {user_uuid} was received completed")
        else:
            print(f"Failed to orders. Status code: {response.status_code}, Response: {response.text}")

    @allure.step("List all orders")
    def list_all_orders(self, user_uuid):
        response = requests.get(
            url=self.endpoints.list_all_orders_for_a_users(user_uuid),
            headers=self.headers.basic_api_17,
        )
        self.attach_response(response.json())
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
