from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.pdf_utils import extract_text_from_pdf
from app.chunk_utils import chunk_text
from app.embedding_utils import create_embedding

from app.crud import (
    create_document,
    create_chunk,
    get_document_by_filename,
    delete_document
)

import shutil
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads"


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    # Create uploads folder
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Check if document already exists
    existing = get_document_by_filename(db, file.filename)

    if existing:
        delete_document(db, existing)

    # Extract text
    text = extract_text_from_pdf(file_path)

    # Split into chunks
    chunks = chunk_text(text)

    # Create new document
    document = create_document(db, file.filename)

    # Save chunks
    for i, chunk in enumerate(chunks):

        embedding = create_embedding(chunk)

        create_chunk(
            db=db,
            document_id=document.id,
            chunk_index=i,
            chunk_text=chunk,
            embedding=embedding
        )

    return {
        "message": "Upload successful",
        "filename": file.filename,
        "total_chunks": len(chunks)
    }