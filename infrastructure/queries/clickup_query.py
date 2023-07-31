import requests
import os
from infrastructure.database.constants import (
    ACCESS_TOKEN_HUBSPOT,
    URL_HUBSPOT
)

headers = {
    'authorization': f"Bearer {ACCESS_TOKEN_HUBSPOT}"
    }


class ClickUpQuery:

    def get_hubspots():
        response = requests.request(
            "GET",
            URL_HUBSPOT,
            headers=headers
        )
        print(response
    )
        all_values = dict(response.json())
        return all_values

    def create_hubspot():
            response = requests.request(
                "POST",
                URL_HUBSPOT,
                headers=headers
            )
            print(response)
            all_values = dict(response.json())
            return all_values
