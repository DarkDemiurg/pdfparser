"""Specific extractor based on `tabula-py` library"""
from io import StringIO
from pathlib import Path

import tabula

from pdfparser.extractors.abc_extractors import CsvExtractor


class TabulaExtractor(CsvExtractor):
    """Specific class for tabula-py extractor"""

    def get_csv(self, filename: Path) -> str:
        """Function for getting CSV from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted CSV
        """
        buf = StringIO()
        dataframes = tabula.read_pdf(filename, pages='all')
        for frame in dataframes:
            buf.write(frame.to_csv(sep=';'))

        return buf.getvalue()
