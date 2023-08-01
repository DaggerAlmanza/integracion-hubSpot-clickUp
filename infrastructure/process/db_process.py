from infrastructure.queries.clickup_query import ClickUpQuery
from infrastructure.database.constants import (
    INTERNAL_SERVER_ERROR,
    OK,
)
from infrastructure.queries.database_query import ApiCallsQuery

repository = ApiCallsQuery()


def save_process(
    data: dict
):
    response = repository.create_query(data)
    if response:
        return {
                "data": response,
                "status_code": OK
            }
    return {
        "error": response,
        "status_code": INTERNAL_SERVER_ERROR
    }


def get_process():
    response = repository.get_query()
    return {
            "data": [data.to_json() for data in response],
            "status_code": OK
        }
