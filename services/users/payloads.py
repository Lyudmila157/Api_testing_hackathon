from faker import Faker

fake = Faker()


class Payloads:
    create_user = {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.first_name(),
        "nickname": fake.user_name()
    }

    list_all_users = {
        "meta": {
            "total": 10
        },
        "users": [
            {
                "email": "max@gmail.com",
                "name": "Max",
                "nickname": "max",
                "avatar_url": "",
                "uuid": "00000000-0000-4562-b3fc-2c963f66afa6"
            }
        ]
    }

    get_a_user_by_email_and_password = {
        "email": "max@gmail.com",
        "password": "password"
    }

    add_an_item_to_user_wishlist = {
        "item_uuid": "00000000-0000-4562-b3fc-2c963f66afa6"
    }

    remove_an_item_to_user_wishlist = {
        "item_uuid": "00000000-0000-4562-b3fc-2c963f66afa6"
    }

    create_a_new_order = {
        "items": [
            {
                "item_uuid": "00000000-0000-4562-b3fc-2c963f66afa6",
                "quantity": 1
            }
        ]
    }