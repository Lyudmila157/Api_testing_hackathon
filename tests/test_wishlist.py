import allure
import pytest
import requests

from config.base_test import BaseTest
from services.users.Update_payloads import UpdatePayloads
from services.users.api_users import UsersAPI


@allure.epic("Users Wishlist")
@allure.feature("Wishlist")
class TestWishlist(BaseTest):

    @pytest.mark.wishlist
    @allure.title("Get a wishlist")
    def test_get_a_wishlist(self):
        user_uuid = self.api_users.get_user()
        if user_uuid:
            self.wishlist_users.get_a_user_wishlist(user_uuid)
        else:
            pytest.fail("User UUID not found. Cannot perform receiving")

    @pytest.mark.wishlist
    @allure.title("Add an item to users wishlist")
    def test_add_an_item_to_users_wishlist(self):
        user_uuid = self.api_users.get_user()
        if user_uuid:
            self.wishlist_users.add_an_item_to_users_wishlist(user_uuid)
        else:
            pytest.fail("User UUID not found. Cannot perform receiving")
