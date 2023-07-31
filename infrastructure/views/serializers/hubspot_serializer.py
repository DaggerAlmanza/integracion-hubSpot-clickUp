from pydantic import BaseModel, Field


class HubspotSerializer(BaseModel):
    company: str = Field(
        ...
    )
    email: str = Field(
        ...
    )
    firstname: str = Field(
        ...
    )
    lastname: str = Field(
        ...
    )
    phone: int = Field(
        ...,
        example=3003003000
    )
    website: str = Field(
        ...,
        example="www.dg.com"
    )