from fastapi import APIRouter
from pydantic import BaseModel
from chatbotBE.services.gpt_service import ask_gpt

router = APIRouter()

class MessageRequest(BaseModel):
    message: str

@router.post("/chatgpt")
def chat_endpoint(request: MessageRequest):
    response = ask_gpt(request.message)
    return {"response": response}
