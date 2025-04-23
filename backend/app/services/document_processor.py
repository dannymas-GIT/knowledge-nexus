import os
import fitz  # PyMuPDF
import docx

class DocumentProcessor:
    """Service for extracting text from documents."""
    def __init__(self):
        pass

    def process_document(self, file_path: str) -> dict:
        """Detect file type and extract full text."""
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            text = self._extract_pdf(file_path)
        elif ext == '.docx':
            text = self._extract_docx(file_path)
        elif ext == '.txt':
            text = self._extract_txt(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        return {'full_text': text}

    def _extract_pdf(self, file_path: str) -> str:
        """Extract text from each page of a PDF."""
        doc = fitz.open(file_path)
        content = ''
        for page in doc:
            content += page.get_text()
        return content

    def _extract_docx(self, file_path: str) -> str:
        """Extract text from a DOCX file."""
        document = docx.Document(file_path)
        return '\n'.join([para.text for para in document.paragraphs])

    def _extract_txt(self, file_path: str) -> str:
        """Read raw text from a TXT file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read() 