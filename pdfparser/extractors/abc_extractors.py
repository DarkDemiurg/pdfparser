"""ABC for text extractors"""
from abc import ABC, abstractmethod
from pathlib import Path


class TextExtractor(ABC):
    """Abstract base class for text extractors"""

    @abstractmethod
    def get_text(self, filename: Path) -> str:
        """Function for getting text from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted text
        """
        pass  # pragma: no cover


class HtmlExtractor(ABC):
    """Abstract base class for HTML extractors"""

    @abstractmethod
    def get_html(self, filename: Path) -> str:
        """Function for getting HTML from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted HTML
        """
        pass  # pragma: no cover


class XmlExtractor(ABC):
    """Abstract base class for XML extractors"""

    @abstractmethod
    def get_xml(self, filename: Path) -> str:
        """Function for getting XML from PDF

        Args:
            filename (pathlib.Path): PDF file path

        Returns:
            str: extracted XML
        """
        pass  # pragma: no cover
