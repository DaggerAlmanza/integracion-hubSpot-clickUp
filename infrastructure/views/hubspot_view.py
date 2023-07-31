from fastapi import APIRouter
from starlette.responses import JSONResponse
from infrastructure.views.serializers.response_serializer import (
    ResponseSerializer
)
from infrastructure.views.serializers.hubspot_serializer import (
    HubspotSerializer
)
from infrastructure.process.hubspot_process import (
    get_process,
    save_process,
)

router = APIRouter()


@router.post(
    "/hubspot",
    tags=["hubspot"],
    response_model=ResponseSerializer
)
async def create_hubspot(
    request: HubspotSerializer
):
    response = save_process(
        request.dict()
    )
    return JSONResponse(
        # status_code=200,
        # content={
        #     "data": "response"
        # }
        status_code=response.pop("status_code"),
        content=response
    )


@router.get(
    "/hubspot",
    tags=["hubspot"],
    response_model=ResponseSerializer
)
async def get_hubspot():
    response = get_process()
    return JSONResponse(
        status_code=response.pop("status_code"),
        content=response
    )
