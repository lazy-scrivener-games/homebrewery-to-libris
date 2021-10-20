# homebrewery-to-libris

Converts Homebrewery formatted markdown to a libris-compatible format.

## Requirements

* Generally assumes a Linux environment.

## Setup

* Install using `pip install homebrewery-to-libris`
* Make sure you use the CSS that can be found [here](https://github.com/lazy-scrivener-games/homebrewery-fork-for-libris/blob/convert-for-enki/phb.standalone.css).
* Make sure you install the TTF fonts that can be found [here](https://github.com/lazy-scrivener-games/homebrewery-fork-for-libris/tree/convert-for-enki/themes/fonts/5e).

## Usage with Libris

* In your libris configuration JSON, add the following property:
```
"markdownPipe": "homebrewery-to-libris"
```

That's it!

## Independent usage

* Run `homebrewery-to-libris < FILE_NAME.md`.

## Homebrewery Note

[Homebrewery](https://homebrewery.naturalcrit.com/) is [copyrighted by Scott Tolksdorf](https://github.com/naturalcrit/homebrewery/blob/master/license). If you like their tool, please consider [supporting its development](https://www.patreon.com/NaturalCrit)!
