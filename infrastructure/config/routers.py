from infrastructure.views import (
    hubspot_view,
    clickup_view
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
