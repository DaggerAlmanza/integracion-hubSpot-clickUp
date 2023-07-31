from fastapi import APIRouter
from starlette.responses import JSONResponse
from infrastructure.views.serializers.response_serializer import ResponseSerializer
# from infrastructure.views.serializers.clickup_serializer import clickupSerializer


router = APIRouter()


# @router.post(
#     "/clickup",
#     tags=["clickup"],
#     response_model=ResponseSerializer
# )
# async def create_clickup(
#     request: clickupSerializer
# ):
#     print(request)
#     # response = clickup_process.save_form(
#     #     request.dict(),
#     #     current_user
#     # )
#     return JSONResponse(
#         status_code=200,
#         content={
#             "data": "response"
#         }
#         # status_code=response.pop("status_code"),
#         # content=response
#     )


@router.get(
    "/clickup",
    tags=["clickup"],
    response_model=ResponseSerializer
)
async def get_clickup():
    # response = clickup_process.get_form(
    #     uuid,
    #     current_user
    # )
    return JSONResponse(
        status_code=200,
        content={
            "data": "response"
        }
        # status_code=response.pop("status_code"),
        # content=response
    )
