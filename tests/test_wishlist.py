import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Users Wishlist")
@allure.feature("Wishlist")
class TestWishlist(BaseTest):

    @pytest.mark.wishlist
    @allure.title("Get user's wishlist")
    def test_get_user_wishlist(self):
        new_user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = new_user.uuid
        user_data = self.api_users.get_a_user(user_uuid)
        print(f"Retrieved User Data: {user_data}")
        assert user_data["uuid"] == user_uuid, "UUID mismatch"
        assert "email" in user_data, "Email is missing"
        wishlist_data = self.wishlist_users.get_user_wishlist(user_uuid)
        assert wishlist_data is not None, "Failed to retrieve wishlist"
        assert len(wishlist_data.get("items", [])) >= 0, "Wishlist is empty or failed"
        # если в вишлисте есть конкретный элемент
        # item_uuid = "00000000-0000-4562-b3fc-2c963f66afa6"
        # items_in_wishlist = [item["uuid"] for item in wishlist_data.get("items", [])]
        # assert item_uuid in items_in_wishlist, f"Item {item_uuid} not found in wishlist"

    # @pytest.mark.wishlist
    # @allure.title("Add an item to user's wishlist")
    # def test_add_an_item_to_users_wishlist_neww(self):
    #     new_user = self.api_users.create_user_with_params()
    #     user_uuid = new_user["uuid"]
    #     user_data = self.api_users.get_a_user(user_uuid)
    #     print(f"Retrieved User Data: {user_data}")
    #     assert user_data["uuid"] == user_uuid, "UUID mismatch"
    #     assert "email" in user_data, "Email is missing"
    #     initial_wishlist = self.wishlist_users.get_user_wishlist(user_uuid)
    #     print(f"Initial Wishlist: {initial_wishlist}")
    #     item_uuid = "00000000-0000-4562-b3fc-2c963f66afa6"
    #     self.wishlist_users.add_an_item_to_users_wishlist(user_uuid, item_uuid)
    #     updated_wishlist = self.wishlist_users.get_user_wishlist(user_uuid)
    #     print(f"Updated Wishlist: {updated_wishlist}")
    #     item_uuids = [item["uuid"] for item in updated_wishlist.get("items", [])]
    #     assert item_uuid in item_uuids, f"Item {item_uuid} was not found in the updated wishlist"

    @pytest.mark.wishlist
    @allure.title("Add an item to users wishlist")
    def test_add_an_item_to_users_wishlist(self):
        new_user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = new_user.uuid
        user_data = self.api_users.get_a_user(user_uuid)
        print(f"Retrieved User Data: {user_data}")
        assert user_data["uuid"] == user_uuid, "UUID mismatch"
        assert "email" in user_data, "Email is missing"
        item_uuid = "00000000-0000-4562-b3fc-2c963f66afa6"
        self.wishlist_users.add_an_item_to_users_wishlist(user_uuid, item_uuid)

    @pytest.mark.wishlist
    @allure.title("Remove an item to users wishlist")
    def test_remove_an_item_to_users_wishlist(self):
        new_user = self.api_users.create_user_and_uuid_with_model_unique()
        user_uuid = new_user.uuid
        user_data = self.api_users.get_a_user(user_uuid)
        print(f"Retrieved User Data: {user_data}")
        assert user_data["uuid"] == user_uuid, "UUID mismatch"
        assert "email" in user_data, "Email is missing"
        # self.wishlist_users.get_user_wishlist(user_uuid)
        self.wishlist_users.remove_an_item_to_users_wishlist(user_uuid)
