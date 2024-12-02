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
        user_uuid = self.api_users.get_user()
        if user_uuid:
            self.orders_users.create_a_new_order(user_uuid)
        else:
            pytest.fail("User UUID not found. Cannot perform receiving")

    @pytest.mark.order
    @allure.title("List all orders")
    def test_list_all_orders(self):
        user_uuid = self.api_users.get_user()
        if user_uuid:
            print(self.orders_users.list_all_orders(user_uuid))
        else:
            pytest.fail("User UUID not found. Cannot perform receiving")

