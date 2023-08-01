import requests
from infrastructure.database.constants import (
    URL_CLICKUP,
    CLIENT_SECRET
)

headers = {"Authorization": CLIENT_SECRET}
task_id = "122"


class ClickUpQuery:

    def get_clickups() -> dict:
        pass

    def create_clickup(propieta: dict):
        try:
            url = f"{URL_CLICKUP}/task/{task_id}"
            headers = {"Authorization": CLIENT_SECRET}
            response = requests.post(url, headers=headers)
            return response
        except Exception as error:
            return f"Error: {error}"
