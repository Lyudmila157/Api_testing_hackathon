import allure
import requests

from utils.helper import Helper
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers
import base64
import os

class AvatarsAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Update user's avatar")
    def update_user_avatar(self, user_uuid, avatar_data):
        # Проверяем существование файла
        if not os.path.exists(avatar_data):
            raise FileNotFoundError(f"Avatar file not found: {avatar_data}")

        url = self.endpoints.update_avatar(user_uuid)
        print(f"Request URL: {url}")

        try:
            # Открываем файл в бинарном режиме
            with open(avatar_data, "rb") as file:
                # Отправляем файл с ключом 'avatar_file', как указано в документации
                files = {"avatar_file": file}  # Здесь мы отправляем файл с ключом 'avatar_file'
                response = requests.put(
                    url=url,
                    headers=self.headers.basic_api_11,  # Убедитесь, что заголовки не содержат 'Content-Type'
                    files=files
                )

            # Логируем ответ
            print(f"Response status code: {response.status_code}")
            try:
                response_data = response.json()
                print(f"Response body: {response_data}")
            except ValueError:
                print(f"Failed to decode JSON. Response text: {response.text}")
                assert False, f"Response is not JSON. Status code: {response.status_code}, Response text: {response.text}"
            assert response.status_code == 200, f"Failed to update avatar. Status code: {response.status_code}, Response: {response.text}"
            self.attach_response(response_data)

            return response_data
        except Exception as e:
            print(f"Error during request: {e}")
            raise e  # Пробрасываем исключение дальше
