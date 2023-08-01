from pydantic import (
    BaseModel,
    Field,
    EmailStr
)


class HubspotSerializer(BaseModel):
    email: EmailStr = Field(
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
        example=3003003000
    )
    website: str = Field(
        ...,
        example="www.dg.com"
    )