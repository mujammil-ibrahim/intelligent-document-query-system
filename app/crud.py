from sqlalchemy.orm import Session

from app.models import Document, DocumentChunk


def get_document_by_filename(db: Session, filename: str):
    return (
        db.query(Document)
        .filter(Document.filename == filename)
        .first()
    )


def delete_document(db: Session, document: Document):

    db.query(DocumentChunk).filter(
        DocumentChunk.document_id == document.id
    ).delete()

    db.delete(document)

    db.commit()


def create_document(db: Session, filename: str):

    document = Document(filename=filename)

    db.add(document)
    db.commit()
    db.refresh(document)

    return document


def create_chunk(
    db: Session,
    document_id: int,
    chunk_index: int,
    chunk_text: str,
    embedding,
):

    chunk = DocumentChunk(
        document_id=document_id,
        chunk_index=chunk_index,
        chunk_text=chunk_text,
        embedding=embedding,
    )

    db.add(chunk)
    db.commit()

    return chunk