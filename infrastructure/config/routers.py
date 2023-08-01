from infrastructure.views import (
    clickup_view,
    hubspot_view
)
from fastapi import APIRouter


urls = APIRouter()


urls.include_router(
    hubspot_view.router,
    prefix="/v1",
)


urls.include_router(
    clickup_view.router,
    prefix="/v1",
)
