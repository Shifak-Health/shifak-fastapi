from pydantic import BaseModel

class GeneratePayloadSchema(BaseModel):
    question: str


class GenerateResponseSchema(BaseModel):
    text: str
