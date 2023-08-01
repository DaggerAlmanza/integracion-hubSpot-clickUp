from fastapi import APIRouter
from starlette.responses import JSONResponse
from infrastructure.views.serializers.response_serializer import ResponseSerializer
from infrastructure.views.serializers.db_serializer import ClickupSerializer
from infrastructure.process.db_process import (
    get_process,
    save_process,
)


router = APIRouter()


@router.post(
    "/db",
    tags=["db"],
    response_model=ResponseSerializer
)
async def create_db(
    request: ClickupSerializer
):
    response = save_process(
        request.model_dump()
    )
    return JSONResponse(
        status_code=response.pop("status_code"),
        content=response
    )


@router.get(
    "/db",
    tags=["db"],
    response_model=ResponseSerializer
)
async def get_db():
    response = get_process()
    return JSONResponse(
        status_code=response.pop("status_code"),
        content=response
    )
