import os

# HOST = "https://dev-gs.qa-playground.com/api/v1"
HOST = "https://release-gs.qa-playground.com/api/v1"


# HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" else "https://release-gs.qa-playground.com/api/v1"


class Endpoints:
    create_user = f"{HOST}/users"
    get_user_by_id = lambda self, uuid: f"{HOST}/users/{uuid}"
    list_all_user = f"{HOST}/users"
    delete_a_user = lambda self, uuid: f"{HOST}/users/{uuid}"
    get_user = f"{HOST}/users"
    update_a_user = lambda self, uuid: f"{HOST}/users/{uuid}"
    get_a_user_by_email_and_password = f"{HOST}/users/login"
    add_an_item_to_users_wishlist = lambda self, uuid: f"{HOST}/users/{uuid}/wishlist/add"
    remove_an_item_to_users_wishlist = lambda self, uuid: f"{HOST}/users/{uuid}/wishlist/remove"
    get_user_wishlist = lambda self, uuid: f"{HOST}/users/{uuid}/wishlist"
    create_a_new_order = lambda self, uuid: f"{HOST}/users/{uuid}/orders"
    list_all_orders_for_a_users = lambda self, uuid: f"{HOST}/users/{uuid}/orders"
    update_avatar = lambda self, uuid: f"{HOST}/users/{uuid}/orders"
