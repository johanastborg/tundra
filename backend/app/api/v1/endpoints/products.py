from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_products():
    return [{"id": 1, "name": "AI Generated Widget"}]
