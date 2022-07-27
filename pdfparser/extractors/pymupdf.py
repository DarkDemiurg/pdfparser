"""Specific extractor based on `PyMuPDF` library"""
from abc import ABC
from io import StringIO
from pathlib import Path

import fitz

from pdfparser.extractors.abc_extractors import HtmlExtractor, TextExtractor, XmlExtractor


class PyMuPDFExtractor(TextExtractor, HtmlExtractor, XmlExtractor, ABC):
    """Specific class for PyMuPDF extractor"""

    def get_text(self, filename: Path) -> str:
        """Function for getting text from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted text
        """
        return self._get(filename, 'text')

    def get_html(self, filename: Path) -> str:
        """Function for getting HTML from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted HTML
        """
        return self._get(filename, 'html')

    def get_xml(self, filename: Path) -> str:
        """Function for getting XML from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted XML
        """
        return self._get(filename, 'xml')

    @staticmethod
    def _get(filename: Path, opt: str = 'html') -> str:
        """Function for getting data from PDF

        Args:
            filename (pathlib.Path): PDF file path
            opt (str): May be 'text', 'xml', 'html'

        Returns:
            str: extracted string
        """
        doc = fitz.open(filename)  # open document
        buf = StringIO()
        if opt == 'xml':
            buf.write('<?xml version="1.0" ?>')
        for page in doc:  # iterate the document pages
            text = page.get_text(opt)  # get plain text (is in UTF-8)
            buf.write(text)  # write text of page

        return buf.getvalue()
