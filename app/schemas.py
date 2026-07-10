from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class RetrievedChunk(BaseModel):
    text: str
    similarity: float


class QueryResponse(BaseModel):
    answer: str
    chunks: list[RetrievedChunk]