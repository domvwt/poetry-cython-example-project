# Adders

A simple Python package demonstrating how to build and package a Cython extension using Poetry.

## Note

Poetry will use the wrong name for the wheel file if you use the `poetry build` command. This is a known issue with Poetry ([#3509](https://github.com/python-poetry/poetry/issues/3509)).
Please use the `make dist` command instead which will rename the wheel file to the correct name.

## Project Structure

```
.
├── build.py             # The build script for compiling Cython extensions
├── Makefile             # Optional Makefile for convenience
├── poetry.lock          # Lock file for Poetry dependencies
├── pyproject.toml       # Poetry configuration file
├── README.md            # This README file
├── src
│   └── adders
│       ├── addition.pyx      # Cython extension file
│       ├── experimental
│       │   ├── addition.pyx  # Experimental Cython extension
│       │   └── __init__.py
│       ├── __init__.py
│       ├── __main__.py
│       └── main.py           # Main Python script
└── tests
    ├── __init__.py
    └── test_addition.py      # Test file for the addition module
```

## Getting Started

### Prerequisites

- Python 3.8.1 or higher
- Poetry
- Cython

### Building the Project

1. Clone the repository:

```
git clone https://github.com/domvwt/poetry-cython-example-project.git
cd adders
```

2. Install the project:

```
make install
```

3. Build the project:

```
make dist
```

### Running the Tests

You can run the tests with the following command:

```
poetry run pytest
```

### Using the Package

You can use the `adders` package in your Python projects like this:

```
from adders import add

result = add(2, 3)
print(result)  # Output: 5
```
