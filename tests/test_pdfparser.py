#!/usr/bin/env python
"""Tests for `pdfparser` package."""

from click.testing import CliRunner

from pdfparser import cli


def test_command_line():
    """Test the CLI help."""
    runner = CliRunner()

    result = runner.invoke(cli.main, args='data/220413.pdf')
    assert result.exit_code == 0

    result = runner.invoke(cli.main, args='../data/220413.pdf')
    assert result.exit_code == 2
    assert "Error: Invalid value for 'FILENAME'" in result.output


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
