[![codecov](https://codecov.io/gh/DarkDemiurg/pdfparser/branch/master/graph/badge.svg?token=tHkHPxsQGr)](https://codecov.io/gh/DarkDemiurg/pdfparser)

# PDF parser
Version 1.0.1

# Author
[DarkDemiurg](mailto:daefimov@gmail.com)

## Features

- Extract text, html, xml or csv from PDF file

## Requirements
### Java
- Java 8+
### Python
- 3.9
- 3.10

```shell
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
```

## Usage

```shell
Usage: pdfparser [OPTIONS] FILENAME

  PDF parser

Options:
  --output-type [TXT|HTML|XML|CSV]
                                  [default: TXT]
  --text_extractor [pdfminer.six|PyPDF2|PyMuPDF|pdftotext]
                                  [default: pdfminer.six]
  --html_extractor [pdfminer.six|pdftables|PyMuPDF]
                                  [default: pdfminer.six]
  --csv_extractor [tabula|pdftables]
                                  [default: tabula]
  --xml_extractor [pdfminer.six|pdftables|PyMuPDF]
                                  [default: pdfminer.six]
  --pdftables_key TEXT            pdftables.com API key
  --output PATH                   Output file name
  --help                          Show this message and exit.

```

## Extractors
- ### [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
- ### [PyPDF2](https://github.com/py-pdf/PyPDF2)
- ### [tabula-py](https://github.com/chezou/tabula-py)
- ### [pymupdf](https://github.com/pymupdf/PyMuPDF)
- ### [pdftotext](https://github.com/jalan/pdftotext)
- ### [pdftables.com](http://pdftables.com) via [python API](https://github.com/pdftables/python-pdftables-api)

### Extractors feature table

| Extractors                                               | TXT |        HTML         | XML  |        CSV         |     | Commercial     |
|----------------------------------------------------------|:---:|:---:|:----:|:------------------:|:---:|:---:|
| [pdfminer.six](https://github.com/pdfminer/pdfminer.six) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |     | :x: |
| [PyPDF2](https://github.com/py-pdf/PyPDF2)               | :heavy_check_mark: | :x: | :x: |        :x:         |     | :x: |
| [tabula-py](https://github.com/chezou/tabula-py)         | :x: | :x: | :x: | :heavy_check_mark: |     | :x: |
| [pymupdf](https://github.com/pymupdf/PyMuPDF)            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |     | :x: |
| [pdftotext](https://github.com/jalan/pdftotext) | :heavy_check_mark: | :x: | :x: |        :x:         |     | :x: |
| [pdftables.com](http://pdftables.com)                    | :x: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |     |  :heavy_check_mark: |

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [DarkDemiurg/cookiecutter-pypackage](https://github.com/DarkDemiurg/cookiecutter-pypackage) project template.
