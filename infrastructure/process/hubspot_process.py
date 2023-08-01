import hubspot

from hubspot.crm.contacts import (
    ApiException,
    SimplePublicObjectInputForCreate,
    SimplePublicObjectInput,
)
from infrastructure.config.helpers import GeneralHelpers
from infrastructure.database.constants import (
    ACCESS_TOKEN_HUBSPOT,
)
from infrastructure.queries.database_query import ApiCallsQuery

repository = ApiCallsQuery()


class HubSpotProcess:

    def __init__(self):
        self.client = hubspot.Client.create(access_token=ACCESS_TOKEN_HUBSPOT)

    def get_contacts(self, after: str = None) -> list:
        try:
            response = self.client.crm.contacts.basic_api.get_page(
                limit=10,
                archived=False,
                after=after
            )
            data = {
                "created_at": GeneralHelpers.get_datetime(),
                "endpoint": "GET-/v1/contact",
                "params": "{}",
                "result": str(response.results[-1].properties),
            }
            print(repository.create_query(data))
            return response
        except ApiException as e:
            data = {
                "created_at": GeneralHelpers.get_datetime(),
                "endpoint": "GET-/v1/contact",
                "params": "{}",
                "result": str(e),
            }
            print(repository.create_query(data.dict()))
            return f"Exception when calling basic_api->get_page: %s\n  % {e}"

    def validate_contact(self, id):
        try:
            response = self.client.crm.contacts.basic_api.get_by_id(
                contact_id=id, properties=["clickup_state"], archived=False
            )
            return response.properties.get('clickup_state')
        except ApiException as e:
            print("Exception when calling basic_api->get_by_id: %s\n" % e)

    def create_contact(self, properties: dict):
        try:
            simple_public_object_input_for_create = SimplePublicObjectInputForCreate(
                properties=properties, associations=[]
            )
            response = self.client.crm.contacts.basic_api.create(
                simple_public_object_input_for_create=simple_public_object_input_for_create
            )
            data = {
                "created_at": GeneralHelpers.get_datetime(),
                "endpoint": "POST-/v1/contact",
                "params": properties,
                "result": str(response.properties),
            }
            print(repository.create_query(data))
            return response.properties
        except ApiException as e:
            data = {
                "created_at": GeneralHelpers.get_datetime(),
                "endpoint": "POST-/v1/contact",
                "params": properties,
                "result": str(e),
            }
            print(repository.create_query(data.dict()))
            return f"Exception when calling basic_api->create: %s\n  % {e}"

    def update_contact(self, id):
        properties = {
            "clickup_state": "true"
        }
        simple_public_object_input = SimplePublicObjectInput(properties=properties)
        try:
            response = self.client.crm.contacts.basic_api.update(
                contact_id=id,
                simple_public_object_input=simple_public_object_input
            )
            return response
        except ApiException as e:
            print("Exception when calling basic_api->update: %s\n" % e)
