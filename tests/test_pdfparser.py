#!/usr/bin/env python
"""Tests for `pdfparser` package."""

from click.testing import CliRunner

from pdfparser import cli
from pdfparser.extractors.pdfminersix import PDFMinerSixExtractor
from pdfparser.extractors.pypdf2 import PyPDF2Extractor
from pdfparser.parser import Parser


def test_command_line():
    """Test the CLI help."""
    runner = CliRunner()

    result = runner.invoke(cli.main, args='data/220413.pdf')
    assert result.exit_code == 0

    result = runner.invoke(cli.main, args='../data/220413.pdf')
    assert result.exit_code == 2
    assert "Error: Invalid value for 'FILENAME'" in result.output


def test_parser():
    parser = Parser()
    assert isinstance(parser.text_extractor, PDFMinerSixExtractor)
    assert isinstance(parser.xml_extractor, PDFMinerSixExtractor)
    assert isinstance(parser.html_extractor, PDFMinerSixExtractor)

    parser.text_extractor = PyPDF2Extractor()
    parser.xml_extractor = PyPDF2Extractor()
    parser.html_extractor = PyPDF2Extractor()
    assert isinstance(parser.text_extractor, PyPDF2Extractor)


def test_pypdf2():
    """Test the CLI help."""
    runner = CliRunner()

    result = runner.invoke(cli.main, args=['--extractor', 'PyPDF2', 'data/220413.pdf'])
    assert result.exit_code == 0


def test_html():
    """Test HTML."""
    runner = CliRunner()

    result = runner.invoke(cli.main, args=['--output-type', 'HTML', 'data/220413.pdf'])
    assert result.exit_code == 0
    assert '<html>' in result.output


def test_xml():
    """Test XML."""
    runner = CliRunner()

    result = runner.invoke(cli.main, args=['--output-type', 'XML', 'data/220413.pdf'])
    assert result.exit_code == 0
    assert '<?xml version="1.0" ?>' in result.output


def test_command_line_help():
    """Test the CLI."""
    runner = CliRunner()

    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    assert "Missing argument 'FILENAME'" in result.output

    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Usage: main [OPTIONS] FILENAME' in help_result.output
    assert '--output-type [TXT|HTML|XML]    [default: TXT]' in help_result.output
    assert '--extractor [pdfminer.six|PyPDF2]' in help_result.output
    assert '--output PATH                   Output file name' in help_result.output
    assert '  --help                          Show this message and exit.' in help_result.output
