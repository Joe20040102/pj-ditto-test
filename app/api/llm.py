from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from ..services.llm_service import stream_generate_response

router = APIRouter()


class LlmRequest(BaseModel):
    text: str


@router.post("/generate-stream")
def generate_text_stream(request: LlmRequest):
    generator = stream_generate_response(request.text)

    return StreamingResponse(generator, media_type="text/plain")
