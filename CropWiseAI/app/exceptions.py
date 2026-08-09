class PDFLoaderError(Exception):
    """Base exception for PDF loading errors."""


class PDFNotFoundError(PDFLoaderError):
    """Raised when the PDF file does not exist."""


class InvalidPDFError(PDFLoaderError):
    """Raised when the PDF cannot be opened."""