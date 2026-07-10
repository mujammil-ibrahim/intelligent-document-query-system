from sqlalchemy.orm import Session
from sqlalchemy import text


def search_similar_chunks(
    db: Session,
    query_embedding,
    limit: int = 3
):
    sql = text("""
        SELECT
            id,
            document_id,
            chunk_index,
            chunk_text,
            embedding <=> CAST(:embedding AS vector) AS distance
        FROM document_chunks
        ORDER BY embedding <=> CAST(:embedding AS vector)
        LIMIT :limit
    """)

    rows = db.execute(
        sql,
        {
            "embedding": str(query_embedding),
            "limit": limit
        }
    ).fetchall()

    unique_chunks = []
    seen = set()

    for row in rows:

        if row.chunk_text in seen:
            continue

        seen.add(row.chunk_text)

        unique_chunks.append({
            "text": row.chunk_text,
            "similarity": round(row.distance, 4)
        })

    return unique_chunks