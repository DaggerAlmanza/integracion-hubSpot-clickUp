from infrastructure.queries.hubspot_query import (
    HubSpotQuery
)
from infrastructure.database.constants import (
    INTERNAL_SERVER_ERROR,
    OK,
)



def save_process(
    clickup: dict
):
    try:
        response = HubSpotQuery.create_hubspot(clickup)
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
        response = HubSpotQuery.get_hubspots()
        return {
                "data": response.get("results", []),
                "status_code": OK
            }
    except Exception as error:
        return {
            "error": error,
            "status_code": INTERNAL_SERVER_ERROR
        }
