import os
from dotenv import load_dotenv

load_dotenv()


class Headers:

    basic = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
    }

    basic_api_1 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-1"
    }

    basic_api_3 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-3"
    }

    basic_api_4 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-4"
    }

    basic_api_6 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-6"
    }

    basic_api_7 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-7"
    }

    basic_api_21 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-21"
    }

    basic_api_22 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-22"
    }

    basic_api_23 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-23"
    }

    basic_api_24 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-24"
    }

    basic_api_5 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-5"
    }

    basic_api_25 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-25"
    }

    basic_api_8 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-8"
    }

    basic_api_16 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-16"
    }

    basic_api_17 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-17"
    }

    basic_api_18 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-18"
    }

    basic_api_11 = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-11"
    }