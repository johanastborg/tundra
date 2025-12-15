from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
async def chat_agent(query: str):
    return {"response": "This is a placeholder for the Google AI agent response."}
