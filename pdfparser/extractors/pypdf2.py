"""Specific extractor based on `PyPDF2` library"""

from io import StringIO
from pathlib import Path

from PyPDF2 import PdfReader

from pdfparser.extractors.abc_extractors import TextExtractor


class PyPDF2Extractor(TextExtractor):
    """Specific class for PyPDF2 extractor"""

    def get_text(self, filename: Path) -> str:
        """Function for getting text from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted text
        """
        reader = PdfReader(filename)
        buf = StringIO()
        number_of_pages = len(reader.pages)
        for page in range(number_of_pages):
            buf.write(reader.pages[page].extract_text())

        return buf.getvalue()
