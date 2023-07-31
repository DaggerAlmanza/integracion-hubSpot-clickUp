from infrastructure.queries.clickup_query import ClickUpQuery
from infrastructure.database.constants import (
    INTERNAL_SERVER_ERROR,
    OK,
)


def save_process(
    clickup: dict
):
    try:
        response = ClickUpQuery.create_clickup(clickup)
        return {
                "data": response.get("results", []),
                "status_code": OK
            }
    except Exception as error:
        return {
            "error": error,
            "status_code": INTERNAL_SERVER_ERROR
        }


def get_process():
    try:
        response = ClickUpQuery.get_clickups()
        return {
                "data": response.get("results", []),
                "status_code": OK
            }
    except Exception as error:
        return {
            "error": error,
            "status_code": INTERNAL_SERVER_ERROR
        }
