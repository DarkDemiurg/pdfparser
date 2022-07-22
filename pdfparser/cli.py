"""Console script for pdfparser."""
from pathlib import Path

import click

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
        parser = Parser()

        if extractor.lower() == 'pypdf2':
            parser = Parser(PyPDF2Extractor())

        result = ''

        output_type = output_type.lower()
        if output_type == 'txt':
            result = parser.get_text(pdf)

        if output_type == 'html':
            result = parser.get_html(pdf)

        if output_type == 'xml':
            result = parser.get_xml(pdf)

        if output is not None:
            with open(output, 'w') as f:
                f.write(result)
        else:
            print(result)
    else:
        click.echo(f'Input PDF file {pdf} does not exists. Abort.')


if __name__ == "__main__":
    main()  # pragma: no cover
