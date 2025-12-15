from fastapi import APIRouter
from app.api.v1.endpoints import products, agents

api_router = APIRouter()

api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
