from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI(
    title="NixOS AWS Demo - FastAPI",
    version="1.0.0",
    description="Backend demo corriendo en NixOS sobre EC2",
)

# Registramos las rutas en / (raíz)
app.include_router(api_router)


# Punto de entrada si lo corres a mano: python main.py
if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
