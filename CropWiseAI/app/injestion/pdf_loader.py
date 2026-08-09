from pathlib import Path
import pymupdf


class PDFLoaderError(Exception):
    """Base exception for PDF loading errors."""


class PDFNotFoundError(PDFLoaderError):
    """Raised when the PDF file does not exist."""


class InvalidPDFError(PDFLoaderError):
    """Raised when the PDF cannot be opened."""
class PDFLoader:
    """
    CLass for loading the pdf
    """
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def load_pdf_apges(
            self,
            start_page = 1,
            end_page: int | None = None
            ):

        #Check fis is exist else return error
        if not self.pdf_path:
            raise PDFNotFoundError(
                f"pdf not found :{self.pdf_path}"
            )
        try:
            document = pymupdf.open(self.pdf_path)
        except pymupdf.FileDataError as exc:
            raise InvalidPDFError(
                    f"Invalid or corrupted PDF: {self.pdf_path}"
                ) from exc

        try:
            total_pages = len(document)
            # Atleast one page should have in the pdf
            if start_page < 1:
                raise ValueError(
                    "start_page must be >= 1"
                )
            #If endpage is none then update end_page as total_page
            if end_page is None:
                end_page = total_pages
            
            #end page should be less than total page
            if end_page > total_pages:
                raise ValueError(
                    f"end_page cannot be greater than "
                    f"{total_pages}"
                )

            pages = []
            for page_number in range(
                start_page, 
                end_page + 1
            ):
                page = document[page_number - 1]
                text = page.get_text().strip()
                pages.append(

                    page_number=page_number,
                    text=text

                )
            return pages

        except Exception as e:
            pass

        
