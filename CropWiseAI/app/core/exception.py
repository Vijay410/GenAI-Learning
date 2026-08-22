class CropWiseException(Exception):
    """Base exception for CropWiseAI."""

class DocumentError(CropWiseException):
    """Base exception for document-related errors."""


class DocumentNotFoundError(DocumentError):
    """Raised when a document cannot be found."""


class UnsupportedDocumentError(DocumentError):
    """Raised when the document type is not supported."""


class DocumentExtractionError(DocumentError):
    """Raised when document text extraction fails."""