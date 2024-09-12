from pydantic import BaseModel

class GeneratePayloadSchema(BaseModel):
    question: str


class SummaryResponseSchema(BaseModel):
    text: str
