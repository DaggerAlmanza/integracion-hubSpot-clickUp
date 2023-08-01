from fastapi import APIRouter
from infrastructure.views import (
    clickup_view,
    hubspot_view,
)


urls = APIRouter()


urls.include_router(
    hubspot_view.router,
    prefix="/v1",
)


urls.include_router(
    clickup_view.router,
    prefix="/v1",
)
