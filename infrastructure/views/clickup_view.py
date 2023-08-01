from fastapi import APIRouter, BackgroundTasks
from infrastructure.database.constants import (
    INTERNAL_SERVER_ERROR,
    OK,
)
from infrastructure.process.clickup_process import (
    ClickUpProcess
)
from infrastructure.views.serializers.response_serializer import ResponseSerializer
from starlette.responses import JSONResponse


router = APIRouter()
clickup_client = ClickUpProcess()


@router.post(
    "/list",
    tags=["clickup"],
    response_model=ResponseSerializer
)
async def create_clickup_task():
    response = clickup_client.create_task()

    return JSONResponse(
        status_code=OK,
        content=response
    )


@router.get(
    "/list",
    tags=["clickup"],
    response_model=ResponseSerializer
)
async def get_clickup_list():
    try:
        response = clickup_client.get()
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


@router.post(
    "/task/",
    tags=["clickup"],
    response_model=ResponseSerializer
)
async def click_up_run_task(background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(run_background_task)
        return JSONResponse(
            status_code=OK,
            content={
                "message": "Tu tarea se está ejecutando y puede tomar tiempo"
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=INTERNAL_SERVER_ERROR,
            content={
                "message": "there was an error"
            }
        )


def run_background_task():
    clickup_client.create_task()
