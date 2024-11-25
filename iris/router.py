from dotenv import load_dotenv
from fastapi import FastAPI

from iris.routers import health_router

load_dotenv()
iris = "iris".upper()
app = FastAPI(title=iris, version="0.1.0")

app.include_router(health_router.router, tags=["health"])
