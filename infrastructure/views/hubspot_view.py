from fastapi import APIRouter
from infrastructure.database.constants import (
    INTERNAL_SERVER_ERROR,
    OK,
)
from infrastructure.process.hubspot_process import (
    HubSpotProcess
)
from infrastructure.views.serializers.hubspot_serializer import (
    HubspotSerializer
)
from infrastructure.views.serializers.response_serializer import (
    ResponseSerializer
)
from starlette.responses import JSONResponse


router = APIRouter()
hubspot_client = HubSpotProcess()


@router.post(
    "/contact",
    tags=["contact"],
    response_model=ResponseSerializer
)
async def create_hubspot(
    request: HubspotSerializer
):
    try:
        response = hubspot_client.create_contact(
            request.model_dump()
        )
        return JSONResponse(
            status_code=OK,
            content=response
        )
    except Exception as e:
        return JSONResponse(
            status_code=INTERNAL_SERVER_ERROR,
            content={
                "message": "there was an error"
            }
        )


@router.get(
    "/contact",
    tags=["contact"],
    response_model=ResponseSerializer
)
async def get_hubspot():
        try:
            response = hubspot_client.get_contacts()
            return JSONResponse(
                content=[data.properties for data in response.results]
            )
        except Exception as e:
            return JSONResponse(
                status_code=INTERNAL_SERVER_ERROR,
                content={
                    "message": "there was an error"
                }
            )
