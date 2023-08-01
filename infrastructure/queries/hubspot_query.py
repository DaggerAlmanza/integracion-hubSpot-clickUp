from infrastructure.config.client_hubspot import (
    client
)
from hubspot.crm.contacts import (
    SimplePublicObjectInputForCreate,
    ApiException
)


class HubSpotQuery:

    def get_hubspots() -> list:
        try:
            response = client.crm.contacts.basic_api.get_page(
                limit=10,
                archived=False
            )
            return response
        except ApiException as e:
            return f"Exception when calling basic_api->get_page: %s\n  % {e}"

    def create_hubspot(properties: dict):
        try:
            simple_public_object_input_for_create = SimplePublicObjectInputForCreate(
                properties=properties, associations=[]
            )
            response = client.crm.contacts.basic_api.create(
                simple_public_object_input_for_create=simple_public_object_input_for_create
            )
            return response
        except ApiException as e:
            return f"Exception when calling basic_api->create: %s\n  % {e}"
