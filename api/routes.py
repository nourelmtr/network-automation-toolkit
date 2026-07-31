from fastapi import APIRouter

from services.network_service import (
    run_ping,
    run_ssh,
)

router = APIRouter()


@router.get("/")
def home():
    return {
        "project": "Network Automation Toolkit",
        "version": "1.0.0",
        "status": "running",
    }


@router.get("/devices")
def devices():
    return run_ping()


@router.post("/ping")
def ping():
    return {
        "devices": run_ping()
    }


@router.post("/backup")
def backup():
    run_ssh()

    return {
        "message": "Backup operation completed."
    }