import allure
import requests

from utils.helper import Helper
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers



class WishlistAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Get user's wishlist by UUID")
    def get_user_wishlist(self, user_uuid):
        url = self.endpoints.get_user_wishlist(user_uuid)
        response = requests.get(
            url=url,
            headers=self.headers.basic_api_5
        )
        self.attach_response(response.json())
        if response.status_code == 200:
            print(f"Successfully retrieved wishlist for user {user_uuid}")
            return response.json()
        else:
            print(f"Failed to retrieve wishlist. Status code: {response.status_code}, Response: {response.text}")
            return None

    # @allure.step("Add an item to users wishlist")
    # def add_an_item_to_users_wishlist(self, user_uuid):
    #     url = self.endpoints.add_an_item_to_users_wishlist(user_uuid)
    #     response = requests.post(
    #         url=url,
    #         headers=self.headers.basic_api_25,
    #         json=self.payloads.add_an_item_to_user_wishlist
    #     )
    #     self.attach_response(response.json())
    #     if response.status_code == 200:
    #         print(f"The wishlist with UUID {user_uuid} was received successfully")
    #     else:
    #         print(f"Failed to wishlist. Status code: {response.status_code}, Response: {response.text}")

    @allure.step("Add an item to users wishlist")
    def add_an_item_to_users_wishlist(self, user_uuid, item_uuid):
        url = self.endpoints.add_an_item_to_users_wishlist(user_uuid)
        response = requests.post(
            url=url,
            headers=self.headers.basic_api_25,
            json={"item_uuid": item_uuid}
        )
        self.attach_response(response.json())
        if response.status_code == 200:
            print(f"The wishlist with UUID {user_uuid} was updated successfully")
        else:
            print(f"Failed to wishlist. Status code: {response.status_code}, Response: {response.text}")

    @allure.step("Remove an item to users wishlist")
    def remove_an_item_to_users_wishlist(self, user_uuid):
        url = self.endpoints.remove_an_item_to_users_wishlist(user_uuid)
        response = requests.post(
            url=url,
            headers=self.headers.basic_api_8,
            json=self.payloads.remove_an_item_to_user_wishlist
        )
        self.attach_response(response.json())
        if response.status_code == 200:
            print(f"Delete with UUID {user_uuid} was delete successfully")
        else:
            print(f"Failed to wishlist. Status code: {response.status_code}, Response: {response.text}")

    # @allure.step("Add an item to user's wishlist")
    # def add_an_item_to_users_wishlist_new(self, user_uuid, item_uuid):
    #     response = requests.post(
    #         url=url,
    #         headers=self.headers.basic_api_25,
    #         json=self.payloads.add_an_item_to_user_wishlist
    #     )
    #     self.attach_response(response.json())

        # if response.status_code == 200:
        #     print(f"Successfully added item {item_uuid} to wishlist for user {user_uuid}. Response: {response.json()}")
        # else:
        #     print(f"Failed to add item to wishlist. Status code: {response.status_code}, Response: {response.text}")

