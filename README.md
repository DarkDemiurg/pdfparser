[![codecov](https://codecov.io/gh/DarkDemiurg/pdfparser/branch/master/graph/badge.svg?token=tHkHPxsQGr)](https://codecov.io/gh/DarkDemiurg/pdfparser)

# PDF parser

PDF parser app

## Features

- Extract text, html, xml or csv from PDF file

## Requirements
### Java
- Java 8+
### Python
- 3.8
- 3.9

## Usage

```shell
Usage: pdfparser [OPTIONS] FILENAME

  PDF parser

Options:
  --output-type [TXT|HTML|XML|CSV]
                                  [default: TXT]
  --text_extractor [pdfminer.six|PyPDF2]
                                  [default: pdfminer.six]
  --output PATH                   Output file name
  --help                          Show this message and exit.

```

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [DarkDemiurg/cookiecutter-pypackage](https://github.com/DarkDemiurg/cookiecutter-pypackage) project template.
