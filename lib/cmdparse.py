# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/FileSensor
# author = i@cdxy.me

"""
FileSensor ver0.2 by <i@cdxy.me>
https://github.com/Xyntax/FileSensor

Usage:
  filesensor.py URL [--404 REGEX] [-o]
  filesensor.py (-h | --help)

Example:
  python3 filesensor.py https://www.cdxy.me --404 "404 File not Found!"

Options:
  -o           save results in ./output folder
  --404 REGEX  filter out custom 404 page with regex
  -h --help    show this help message

"""

from docopt import docopt


def get_arguments():
    return docopt(__doc__)
