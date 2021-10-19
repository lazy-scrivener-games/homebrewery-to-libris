# homebrewery-to-enki

Converts [Homebrewery](https://homebrewery.naturalcrit.com/) formatted markdown to an enki-compatible format.

## Requirements

* Generally assumes a Linux environment, but may work with Windows. All of my Windows testing uses [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install).
* Python 3.x

## Setup

* Go into the top-level project folder and install the module using pip3 install .

## Standalone Usage

* Run `homebrewery-to-enki < FILE_NAME.md`.

## Usage with Enki

* Add a "markdownPipe" property to your enki config file that has the value "homebrewery-to-enki". Assuming homebrewery-to-enki is properly installed and on your system path, this will apply the effects to your files.
