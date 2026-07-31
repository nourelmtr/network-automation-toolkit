from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router

app = FastAPI(
    title="Network Automation Toolkit",
    version="1.0.0",
    description="REST API for network automation."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)