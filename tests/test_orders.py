
import allure
import pytest
import requests

from config.base_test import BaseTest
from services.users.Update_payloads import UpdatePayloads


@allure.epic("Users Orders")
@allure.feature("Orders")
class TestOrders(BaseTest):

    @pytest.mark.order
    @allure.title("Create a new order")
    def test_create_a_new_order(self):
        user_uuid = self.api_users.create_user_and_uuid_with_model_unique()
        print(f"User UUID in test: {user_uuid}")
        if user_uuid:
            self.api_opders.create_a_new_order(user_uuid)
        else:
            pytest.fail("User UUID not found. Cannot perform receiving")

    @pytest.mark.order
    @allure.title("List all orders")
    def test_list_all_orders(self):
        user_uuid = self.api_users.create_user_and_uuid_with_model_unique()
        print(f"User UUID: {user_uuid}")
        self.api_opders.create_a_new_order(user_uuid)
        if user_uuid:
            orders = self.api_opders.list_all_orders(user_uuid)
            print(f"Orders list: {orders}")
        else:
            pytest.fail("User UUID not found. Cannot perform receiving")

    # @pytest.mark.order
    # @allure.title("Create a new order new")
    # def test_create_a_new_order_new(self):
    #     user = self.api_users.create_user_and_uuid_with_model_unique()
    #     user_uuid = user.uuid
    #     print(f"User UUID in test: {user_uuid}")
    #     if user_uuid:
    #         self.api_opders.create_a_new_order_new(user_uuid)
    #     else:
    #         pytest.fail("User UUID not found. Cannot perform receiving")

