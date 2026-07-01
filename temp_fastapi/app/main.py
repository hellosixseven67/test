from fastapi import FastAPI
from app.routes.hello import router as hello_router

app = FastAPI(title="Temp FastAPI Project")

app.include_router(hello_router, prefix="/api")
