"""Console script for pdfparser."""
from pathlib import Path

import click

from pdfparser.extractors.pdfminersix import PDFMinerSixExtractor
from pdfparser.extractors.pypdf2 import PyPDF2Extractor
from pdfparser.parser import Parser


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option(
    '--output-type', default='TXT', show_default=True, type=click.Choice(['TXT', 'HTML', 'XML'], case_sensitive=False)
)
@click.option(
    '--extractor',
    default='pdfminer.six',
    show_default=True,
    type=click.Choice(['pdfminer.six', 'PyPDF2'], case_sensitive=False),
)
@click.option('--output', type=click.Path(), help='Output file name')
def main(filename: str, output_type: str, extractor: str, output: str) -> None:
    """PDF parser"""
    click.echo("pdfparser")
    click.echo("=" * len("pdfparser"))
    click.echo(f"PDF file is {click.format_filename(filename)}")

    pdf = Path(filename)

    if pdf.exists():
        parser = Parser(PDFMinerSixExtractor())
        with open('result_pdfminer.txt', 'w') as f:
            f.write(parser.get_text(pdf))

        parser.text_extractor = PyPDF2Extractor()
        with open('result_pypdf2.txt', 'w') as f:
            f.write(parser.get_text(pdf))
    else:
        click.echo(f'Input PDF file {pdf} does not exists. Abort.')


if __name__ == "__main__":
    main()  # pragma: no cover
