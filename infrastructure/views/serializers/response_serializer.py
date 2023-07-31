from typing import Optional
from pydantic import BaseModel, Field


class ResponseSerializer(BaseModel):
    message: str = Field(
        ...,
    )
    data: Optional[dict] = Field(
        None,
        description="Data for response"
    )
    error: Optional[list or dict] = Field(
        None,
        description="Error for response"
    )
