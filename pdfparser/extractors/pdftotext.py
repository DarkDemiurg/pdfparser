"""Specific extractor based on `pdftotext` library"""

from abc import ABC
from io import StringIO
from pathlib import Path

import pdftotext

from pdfparser.extractors.abc_extractors import TextExtractor


class PDFtoTextExtractor(TextExtractor, ABC):
    """Specific class for pdftotext extractor"""

    def get_text(self, filename: Path) -> str:
        """Function for getting text from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted text
        """
        buf = StringIO()
        with open(filename, "rb") as f:
            pdf = pdftotext.PDF(f)

            for page in pdf:
                buf.write(page)

        return buf.getvalue()
