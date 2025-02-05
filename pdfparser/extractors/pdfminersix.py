"""Specific extractor based on `pdfminer.six` library"""

from abc import ABC
from io import StringIO
from pathlib import Path

from pdfminer.high_level import extract_text, extract_text_to_fp
from pdfminer.layout import LAParams

from pdfparser.extractors.abc_extractors import HtmlExtractor, TextExtractor, XmlExtractor


class PDFMinerSixExtractor(TextExtractor, HtmlExtractor, XmlExtractor, ABC):
    """Specific class for pdfminer.six extractor"""

    def get_text(self, filename: Path) -> str:
        """Function for getting text from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted text
        """
        return extract_text(filename)

    def get_html(self, filename: Path) -> str:
        """Function for getting HTML from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted HTML
        """
        return self._get(filename)

    def get_xml(self, filename: Path) -> str:
        """Function for getting XML from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted XML
        """
        return self._get(filename, 'xml')

    @staticmethod
    def _get(filename: Path, output_type: str = 'html') -> str:
        """Function for getting data from PDF

        Args:
            filename (pathlib.Path): PDF file path
            output_type (str): May be 'text', 'xml', 'html', 'tag'.

        Returns:
            str: extracted string
        """
        output_string = StringIO()
        with open(filename, 'rb') as fin:
            extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type=output_type, codec='')
        return output_string.getvalue()
