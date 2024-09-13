from fastapi import APIRouter
from app.models.pydantic import GeneratePayloadSchema, GenerateResponseSchema
from app.models.gpt2 import answer_question

router = APIRouter()

@router.post("/", response_model=GenerateResponseSchema, status_code=201)
async def create_summary(
    payload: GeneratePayloadSchema
) -> GeneratePayloadSchema:
    return {"text": answer_question(payload.question)}