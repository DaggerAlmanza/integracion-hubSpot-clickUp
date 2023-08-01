import hubspot
from infrastructure.database.constants import (
    ACCESS_TOKEN_HUBSPOT,
)


client = hubspot.Client.create(access_token=ACCESS_TOKEN_HUBSPOT)
