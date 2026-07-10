from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import QueryRequest, QueryResponse
from app.embedding_utils import create_embedding
from app.search import search_similar_chunks
from app.llm import ask_llm

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
async def query_document(
    request: QueryRequest,
    db: Session = Depends(get_db)
):
    # Generate embedding
    query_embedding = create_embedding(request.question)

    # Retrieve similar chunks
    chunks = search_similar_chunks(db, query_embedding)

    # Build context for LLM
    context = "\n\n".join(
        chunk["text"] for chunk in chunks
    )

    # Ask LLM
    answer = ask_llm(
        question=request.question,
        context=context
    )

    return QueryResponse(
        answer=answer,
        chunks=chunks
    )