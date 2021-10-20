# homebrewery-to-libris

Converts Homebrewery formatted markdown to an libris-compatible format.

## Requirements

* Generally assumes a Linux environment.

## Setup

* Install using `pip install homebrewery-to-libris`

## Usage with Libris

* In your libris configuration JSON, add the following property:
```
"markdownPipe": "homebrewery-to-libris"
```

That's it!

## Independent usage

* Run `homebrewery-to-libris < FILE_NAME.md`.
