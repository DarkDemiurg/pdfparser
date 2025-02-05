"""Console script for pdfparser."""

from pathlib import Path

import click

from pdfparser.extractors.pdftables import PdfTablesExtractor
from pdfparser.extractors.pdftotext import PDFtoTextExtractor
from pdfparser.extractors.pymupdf import PyMuPDFExtractor
from pdfparser.extractors.pypdf2 import PyPDF2Extractor
from pdfparser.parser import Parser


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option(
    '--output-type',
    default='TXT',
    show_default=True,
    type=click.Choice(['TXT', 'HTML', 'XML', 'CSV'], case_sensitive=False),
)
@click.option(
    '--text_extractor',
    default='pdfminer.six',
    show_default=True,
    type=click.Choice(['pdfminer.six', 'PyPDF2', 'PyMuPDF', 'pdftotext'], case_sensitive=False),
)
@click.option(
    '--html_extractor',
    default='pdfminer.six',
    show_default=True,
    type=click.Choice(['pdfminer.six', 'pdftables', 'PyMuPDF'], case_sensitive=False),
)
@click.option(
    '--csv_extractor',
    default='tabula',
    show_default=True,
    type=click.Choice(['tabula', 'pdftables'], case_sensitive=False),
)
@click.option(
    '--xml_extractor',
    default='pdfminer.six',
    show_default=True,
    type=click.Choice(['pdfminer.six', 'pdftables', 'PyMuPDF'], case_sensitive=False),
)
@click.option('--pdftables_key', type=str, help='pdftables.com API key')
@click.option('--output', type=click.Path(), help='Output file name')
def main(
    filename: str,
    output_type: str,
    text_extractor: str,
    html_extractor: str,
    csv_extractor: str,
    xml_extractor: str,
    pdftables_key: str,
    output: str,
) -> None:
    """PDF parser"""
    click.echo("pdfparser")
    click.echo("=" * len("pdfparser"))
    click.echo(f"PDF file is {click.format_filename(filename)}")

    pdf = Path(filename)

    parser = Parser()

    if text_extractor.lower() == 'pypdf2':
        parser.text_extractor = PyPDF2Extractor()

    if text_extractor.lower() == 'pymupdf':
        parser.text_extractor = PyMuPDFExtractor()

    if text_extractor.lower() == 'pdftotext':
        parser.text_extractor = PDFtoTextExtractor()

    if csv_extractor.lower() == 'pdftables':
        if pdftables_key is not None:
            parser.csv_extractor = PdfTablesExtractor(pdftables_key)
        else:
            click.echo("Require pdftables.com API key for working. Abort.")

    if html_extractor.lower() == 'pdftables':
        if pdftables_key is not None:
            parser.html_extractor = PdfTablesExtractor(pdftables_key)
        else:
            click.echo("Require pdftables.com API key for working. Abort.")

    if html_extractor.lower() == 'pymupdf':
        parser.html_extractor = PyMuPDFExtractor()

    if xml_extractor.lower() == 'pdftables':
        if pdftables_key is not None:
            parser.xml_extractor = PdfTablesExtractor(pdftables_key)
        else:
            click.echo("Require pdftables.com API key for working. Abort.")

    if xml_extractor.lower() == 'pymupdf':
        parser.xml_extractor = PyMuPDFExtractor()

    methods = {
        'txt': parser.get_text,
        'html': parser.get_html,
        'xml': parser.get_xml,
        'csv': parser.get_csv,
    }

    result = methods[output_type.lower()](pdf)

    if output is not None:
        with open(output, 'w') as f:
            f.write(result)
    else:
        print(result)


if __name__ == "__main__":
    main()  # pragma: no cover
