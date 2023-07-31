from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from infrastructure.config import routers


urls = APIRouter()


app = FastAPI(
    title="API Integración de HubSpot y ClickUp.",
    description="Permita crear contactos en HubSpot y sincronizarlos con ClickUp",
    version="1.0.0",
    redoc_url="/redoc"
)

app.include_router(
    routers.urls,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
