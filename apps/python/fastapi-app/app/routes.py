from fastapi import APIRouter
from datetime import datetime
import platform
import os

router = APIRouter()


@router.get("/")
def root():
    """
    Endpoint principal: devuelve info de la demo.
    """
    return {
        "service": "fastapi-backend",
        "message": "Hola desde FastAPI en NixOS sobre EC2 🚀",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "hostname": platform.node(),
        "python_version": platform.python_version(),
        "environment": {
            "PORT": os.getenv("PORT", "8000"),
        },
    }


@router.get("/health")
def health():
    """
    Endpoint de healthcheck muy simple.
    """
    return {"status": "ok"}
