"""Main module."""

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
        """Constructor"""
        self._text_extractor = text_extractor
        self._xml_extractor = xml_extractor
        self._html_extractor = html_extractor

    @property
    def text_extractor(self) -> TextExtractor:
        """Current text extractor"""
        return self._text_extractor

    @text_extractor.setter
    def text_extractor(self, extractor: TextExtractor) -> None:
        """Current text extractor setter"""
        self._text_extractor = extractor

    @property
    def xml_extractor(self) -> XmlExtractor:
        """Current XML extractor"""
        return self._xml_extractor

    @xml_extractor.setter
    def xml_extractor(self, xml_extractor: XmlExtractor) -> None:
        """Current XML extractor setter"""
        self._xml_extractor = xml_extractor

    @property
    def html_extractor(self) -> HtmlExtractor:
        """Current HTML extractor"""
        return self._html_extractor

    @html_extractor.setter
    def html_extractor(self, html_extractor: HtmlExtractor) -> None:
        """Current HTML extractor setter"""
        self._html_extractor = html_extractor

    def get_text(self, filename: Path) -> str:
        """Function for getting text from PDF"""
        return self._text_extractor.get_text(filename)

    def get_xml(self, filename: Path) -> str:
        """Function for getting XML from PDF"""
        return self._xml_extractor.get_xml(filename)

    def get_html(self, filename: Path) -> str:
        """Function for getting HTML from PDF"""
        return self._html_extractor.get_html(filename)
