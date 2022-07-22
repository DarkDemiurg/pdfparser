"""Parser module."""

from pathlib import Path

from pdfparser.extractors.abc_extractors import HtmlExtractor, TextExtractor, XmlExtractor
from pdfparser.extractors.pdfminersix import PDFMinerSixExtractor


class Parser:
    """Class for parse PDF documents"""

    def __init__(
        self,
        text_extractor: TextExtractor = PDFMinerSixExtractor(),
        xml_extractor: XmlExtractor = PDFMinerSixExtractor(),
        html_extractor: HtmlExtractor = PDFMinerSixExtractor(),
    ) -> None:
        """Constructor

        Args:
            text_extractor (TextExtractor): extractor for text
            xml_extractor (XmlExtractor): extractor for XML
            html_extractor (HtmlExtractor): extractor for HTML
        """
        self._text_extractor = text_extractor
        self._xml_extractor = xml_extractor
        self._html_extractor = html_extractor

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
