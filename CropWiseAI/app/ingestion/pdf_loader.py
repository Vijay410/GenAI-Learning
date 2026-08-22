from pathlib import Path
import sys

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import pymupdf

from app.core.exception import (
    DocumentExtractionError,
    DocumentNotFoundError,
    UnsupportedDocumentError,
)


class PDFLoader:
    """Load text from a PDF document."""

    def load(self, file_path: str) -> str:
        path = Path(file_path)

        if not path.exists():
            raise DocumentNotFoundError(
                f"Document not found: {file_path}"
            )

        if path.suffix.lower() != ".pdf":
            raise UnsupportedDocumentError(
                f"Unsupported document type: {path.suffix}"
            )

        try:
            document = pymupdf.open(path)

            try:
                text = ""

                for page in document:
                    text += page.get_text()

                return text

            finally:
                document.close()

        except Exception as exc:
            raise DocumentExtractionError(
                f"Failed to extract text from: {file_path}"
            ) from exc