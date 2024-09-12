from fastapi import APIRouter, BackgroundTasks
from app.models.pydantic import GeneratePayloadSchema, GenerateResponseSchema

router = APIRouter()

@router.post("/", response_model=GenerateResponseSchema, status_code=201)
async def create_summary(
    payload: GeneratePayloadSchema, background_tasks: BackgroundTasks
) -> GeneratePayloadSchema:
    return {"text": ""}