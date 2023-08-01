import requests

from infrastructure.database.constants import (
    CLIENT_SECRET,
    LIST_ID_CLICKUP,
    URL_CLICKUP,
)
from infrastructure.process.hubspot_process import HubSpotProcess

headers = {"Authorization": CLIENT_SECRET}


class ClickUpProcess:

    def __init__(self) -> None:
        self.hubspot_client = HubSpotProcess()
        self.header = {
            "Content-Type": "application/json",
            "Authorization": CLIENT_SECRET
        }
        self.url = URL_CLICKUP
        self.after_contact = "45151"
        self.after_max = "-1"
        self.contacts = None

    def get(self) -> dict:
        response = requests.get(
            self.url+"/list/"+LIST_ID_CLICKUP,
            headers=self.header)
        return dict(response.json())

    def create_task(self) -> dict:

        while int(self.after_contact) > int(self.after_max):
            self.after_max = self.after_contact
            self.__get_contacts(after=self.after_contact)
            for contact in self.contacts:
                if not self.hubspot_client.validate_contact(
                    contact.get("hs_object_id")
                ):
                    print(contact.get("hs_object_id"))
                    result = self.__create_task(contact)
                    self.hubspot_client.update_contact(contact.get("hs_object_id"))
        return {
            "message": "La tarea ha finalizado"
        }

    def __get_contacts(self, after=None):
        response = self.hubspot_client.get_contacts(after=after)
        self.contacts = [data.properties for data in response.results]
        if response.paging:
            self.after_contact = response.paging.next.after

    def __create_task(self, data: dict):
        url = self.__get_url("list")+ LIST_ID_CLICKUP + "/task"
        return requests.post(
            url,
            headers=self.header,
            json=self.__get_task_payload(data)
        )

    def __get_url(self, resource: str):
        return f"{self.url}{resource}/"

    def __get_task_payload(self, data: dict):
        return {
            "name": f"Agregar tarea {data['hs_object_id']}",
            "description": f"Agregando a {data.get('firstname')} {data.get('lastname')} contacto en tarea",
        }
