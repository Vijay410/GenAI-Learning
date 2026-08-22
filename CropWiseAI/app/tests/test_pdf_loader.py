import pytest

from app.ingestion.pdf_loader import PDFLoader

from app.core.exception import (
    DocumentExtractionError,
    DocumentNotFoundError,
    UnsupportedDocumentError,
)

PDF_PATH = (
    "app/data/raw/Tomato-Diseases-and-Disorders.pdf"
)

def test_pdf_loader_load_success():
    loader = PDFLoader()
    text = loader.load(PDF_PATH)
    assert isinstance(text, str)
    assert len(text) > 0

def test_pdf_Loader_Load_file_not_found():
    loader = PDFLoader()
    with pytest.raises(DocumentNotFoundError):
        loader.load("non_existent_file.pdf")