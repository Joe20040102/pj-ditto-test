from fastapi import APIRouter
from pydantic import BaseModel

from ..services import llm_service

router = APIRouter()


class LlmRequest(BaseModel):
    text: str


@router.post("/generate")
def generate_text(request: LlmRequest):
    response = llm_service.generate_response(request.text)
    return {"response": response}
