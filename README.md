[![codecov](https://codecov.io/gh/DarkDemiurg/pdfparser/branch/master/graph/badge.svg?token=tHkHPxsQGr)](https://codecov.io/gh/DarkDemiurg/pdfparser)

# PDF parser
Version 0.4.0

# Author
[DarkDemiurg](mailto:daefimov@gmail.com)

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
  --html_extractor [pdfminer.six|pdftables]
                                  [default: pdfminer.six]
  --csv_extractor [tabula|pdftables]
                                  [default: tabula]
  --pdftables_key TEXT            pdftables.com API key
  --output PATH                   Output file name
  --help                          Show this message and exit.
```

## Extractors
- ### [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
- ### [PyPDF2](https://github.com/py-pdf/PyPDF2)
- ### [tabula-py](https://github.com/chezou/tabula-py)
- ### [pdftables.com](pdftables.com) via [python API](https://github.com/pdftables/python-pdftables-api)

### Extractors feature table

| Extractors/Type                                          | TXT |        HTML         | XML  | CSV   |
|----------------------------------------------------------|:---:|:-------------------:|:----:|:-----:|
| [pdfminer.six](https://github.com/pdfminer/pdfminer.six) | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
| [PyPDF2](https://github.com/py-pdf/PyPDF2)               | :heavy_check_mark: | :x: | :x: | :x: |
| [tabula-py](https://github.com/chezou/tabula-py)         | :x: | :x: | :x: | :heavy_check_mark: |
| [pdftables.com](pdftables.com)                           | :x: | :heavy_check_mark: | :x: | :heavy_check_mark: |

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [DarkDemiurg/cookiecutter-pypackage](https://github.com/DarkDemiurg/cookiecutter-pypackage) project template.
