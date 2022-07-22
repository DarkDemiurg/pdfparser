"""Specific extractor based on `pdftables` library"""
from pathlib import Path

import pdftables_api

from pdfparser.extractors.abc_extractors import CsvExtractor, HtmlExtractor


class PdfTablesExtractor(CsvExtractor, HtmlExtractor):
    """Specific class for pdftables extractor"""

    def __init__(self, api_key: str):
        """Constructor

        Args:
            api_key (str): pdftables.com API key
        """
        self._api_key = api_key

    def get_html(self, filename: Path) -> str:
        """Function for getting HTML from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted HTML
        """
        client = pdftables_api.Client(self._api_key)
        return client.html(filename)

    def get_csv(self, filename: Path) -> str:
        """Function for getting CSV from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted CSV
        """
        client = pdftables_api.Client(self._api_key)
        return client.csv(filename)
