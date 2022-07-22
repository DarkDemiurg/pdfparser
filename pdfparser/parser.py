"""Parser module."""

from pathlib import Path

from pdfparser.extractors.abc_extractors import CsvExtractor, HtmlExtractor, TextExtractor, XmlExtractor
from pdfparser.extractors.pdfminersix import PDFMinerSixExtractor
from pdfparser.extractors.tabulapy import TabulaExtractor


class Parser:
    """Class for parse PDF documents"""

    def __init__(
        self,
        text_extractor: TextExtractor = PDFMinerSixExtractor(),
        xml_extractor: XmlExtractor = PDFMinerSixExtractor(),
        html_extractor: HtmlExtractor = PDFMinerSixExtractor(),
        csv_extractor: CsvExtractor = TabulaExtractor(),
    ) -> None:
        """Constructor

        Args:
            text_extractor (TextExtractor): extractor for text
            xml_extractor (XmlExtractor): extractor for XML
            html_extractor (HtmlExtractor): extractor for HTML
            csv_extractor (CsvExtractor): extractor for CSV
        """
        self._text_extractor = text_extractor
        self._xml_extractor = xml_extractor
        self._html_extractor = html_extractor
        self._csv_extractor = csv_extractor

    @property
    def text_extractor(self) -> TextExtractor:
        """Current text extractor

        Returns:
            TextExtractor: current text extractor object
        """
        return self._text_extractor

    @text_extractor.setter
    def text_extractor(self, extractor: TextExtractor) -> None:
        """Current text extractor setter

        Args:
            extractor (TextExtractor): new text extractor object

        Returns:
            None: None
        """
        self._text_extractor = extractor

    @property
    def xml_extractor(self) -> XmlExtractor:
        """Current XML extractor

        Returns:
            XmlExtractor: current XML extractor object
        """
        return self._xml_extractor

    @xml_extractor.setter
    def xml_extractor(self, xml_extractor: XmlExtractor) -> None:
        """Current XML extractor setter

        Args:
            xml_extractor (XmlExtractor): new XML extractor object

        Returns:
            None: None
        """
        self._xml_extractor = xml_extractor

    @property
    def html_extractor(self) -> HtmlExtractor:
        """Current HTML extractor

        Returns:
            HtmlExtractor: current HTML extractor object
        """ ""
        return self._html_extractor

    @html_extractor.setter
    def html_extractor(self, html_extractor: HtmlExtractor) -> None:
        """Current HTML extractor setter

        Args:
            html_extractor (HtmlExtractor): new HTML extractor object

        Returns:
            None: None
        """
        self._html_extractor = html_extractor

    @property
    def csv_extractor(self) -> CsvExtractor:
        """Current CSV extractor

        Returns:
            CsvExtractor: current CSV extractor object
        """ ""
        return self._csv_extractor

    @csv_extractor.setter
    def csv_extractor(self, csv_extractor: CsvExtractor) -> None:
        """Current CSV extractor setter

        Args:
            csv_extractor (CsvExtractor): new CSV extractor object

        Returns:
            None: None
        """
        self._csv_extractor = csv_extractor

    def get_text(self, filename: Path) -> str:
        """Function for getting text from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted text
        """
        return self._text_extractor.get_text(filename)

    def get_xml(self, filename: Path) -> str:
        """Function for getting XML from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted XML
        """
        return self._xml_extractor.get_xml(filename)

    def get_html(self, filename: Path) -> str:
        """Function for getting HTML from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted HTML
        """
        return self._html_extractor.get_html(filename)

    def get_csv(self, filename: Path) -> str:
        """Function for getting CSV from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted CSV
        """
        return self._csv_extractor.get_csv(filename)
