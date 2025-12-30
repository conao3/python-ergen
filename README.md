# ergen

A command-line tool for generating Entity-Relationship Diagrams from YAML definitions.

[![License](https://img.shields.io/github/license/conao3/python-ergen.svg?style=flat-square)](https://github.com/conao3/python-ergen/blob/master/LICENSE)
[![Release](https://img.shields.io/github/tag/conao3/python-ergen.svg?style=flat-square)](https://github.com/conao3/python-ergen/releases)

## Overview

ergen simplifies database documentation by generating ERD diagrams from a single YAML source file. Define your tables and relationships in YAML, and ergen outputs Graphviz DOT format that can be rendered into visual diagrams.

## Features

- Define database schemas in human-readable YAML
- Generate Graphviz DOT files for ER diagrams
- Support for foreign key relationships with automatic edge rendering
- Column type annotations and constraints

## Installation

```bash
pip install ergen
```

Or with Poetry:

```bash
poetry add ergen
```

## Usage

### Basic Command

```bash
ergen er schema.yaml
```

### YAML Schema Format

Define your database schema in YAML:

```yaml
version: 1.0
title: "My Database Schema"
tables:
  - name: users
    columns:
      - name: id
        type: INTEGER
        primary_key: true
      - name: email
        type: VARCHAR
        type_arg1: 255
        unique: true
      - name: created_at
        type: TIMESTAMP

  - name: posts
    columns:
      - name: id
        type: INTEGER
        primary_key: true
      - name: user_id
        type: INTEGER
        foreign_key:
          ref_table: users
          ref_column: id
      - name: title
        type: VARCHAR
        type_arg1: 200
      - name: content
        type: TEXT
        nullable: true
```

### Generating Diagrams

Generate a DOT file and render it with Graphviz:

```bash
ergen er schema.yaml > schema.dot
dot -Tpng schema.dot -o schema.png
```

## Requirements

- Python 3.9 or higher

## Contributing

Contributions are welcome. Feel free to open issues for bug reports or feature requests, and submit pull requests for improvements.

## License

Apache License 2.0 - see [LICENSE](LICENSE) for details.

## Author

Naoya Yamashita ([@conao3](https://github.com/conao3))
