from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import tempfile
from app.services.document_processor import DocumentProcessor

router = APIRouter()
processor = DocumentProcessor()

@router.post("/documents/process")
async def process_document(file: UploadFile = File(...)):
    """
    Upload a document file and return extracted full text.
    """
    tmp_path = None
    try:
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            contents = await file.read()
            tmp.write(contents)
            tmp.flush()
            tmp_path = tmp.name
        result = processor.process_document(tmp_path)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path) 