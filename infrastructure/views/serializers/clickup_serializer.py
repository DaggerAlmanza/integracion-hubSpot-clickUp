from pydantic import BaseModel, Field


class HubspotSerializer(BaseModel):
    email: bool = Field(
        ...
    )
    firstname: str = Field(
        ...
    )
    lastname: str = Field(
        ...
    )
    phone: str = Field(
        ...,
        example="3003003000"
    )
    website: str = Field(
        ...,
        example="www.dg.com"
    )