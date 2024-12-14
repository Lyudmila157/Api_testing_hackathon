
import allure
import requests

from utils.helper import Helper
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers
from services.users.endpoints import HOST


class OrdersApi(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create a new order")
    def create_a_new_order(self, user_uuid):
        url = self.endpoints.create_a_new_order(user_uuid)
        print(f"Request URL: {url}")
        print(f"Payload being sent: {self.payloads.create_a_new_order}")
        response = requests.post(
            url=url,
            headers=self.headers.basic_api_16,
            json=self.payloads.create_a_new_order
        )
        print(f"Status code: {response.status_code}, Response text: {response.text}")

        if response.status_code == 200:
            print(f"User with UUID {user_uuid} successfully.")
        else:
            try:
                response_data = response.json()
                self.attach_response(response_data)
            except ValueError:
                print(
                    f"Failed to decode JSON. Response is not JSON. Status code: {response.status_code}, Response text: {response.text}")

    @allure.step("List all orders")
    def list_all_orders(self, user_uuid):
        url = self.endpoints.list_all_orders_for_a_users(user_uuid)
        print(f"Request URL: {url}")
        response = requests.get(
            url=url,
            headers=self.headers.basic_api_17,
        )
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        self.attach_response(response.json())
        return response.json()

    @allure.step("Create a new order new")
    def create_a_new_order_new(self, user_uuid):
        url = self.endpoints.create_a_new_order(user_uuid)
        print(f"Request URL: {url}")
        payload = self.payloads.create_a_new_order
        print(f"Payload being sent: {payload}")
        response = requests.post(
            url=url,
            headers=self.headers.basic_api_16,
            json=payload
        )
        print(f"Status code: {response.status_code}, Response text: {response.text}")
        if response.status_code == 200:
            print(f"Order successfully created for user UUID {user_uuid}.")
        else:
            try:
                response_data = response.json()
                self.attach_response(response_data)
            except ValueError:
                print(
                    f"Failed to decode JSON. Status code: {response.status_code}, Response text: {response.text}")
            response.raise_for_status()
