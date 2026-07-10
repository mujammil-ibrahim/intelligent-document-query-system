from sqlalchemy.orm import Session
from app.models import Document, DocumentChunk


def save_document(db: Session, filename: str):
    doc = Document(filename=filename)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc


def save_chunks(db: Session, document_id: int, chunks: list[str]):
    for i, chunk in enumerate(chunks):
        db.add(
            DocumentChunk(
                document_id=document_id,
                chunk_index=i,
                chunk_text=chunk
            )
        )

    db.commit()