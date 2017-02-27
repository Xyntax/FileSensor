"""
FileSensor version 0.1 by Xyntax@github.com

Usage:
  filesensor.py URL
  filesensor.py (-u URL | -f FILE)
  filesensor.py (-h | --help)

Options:
  -u URL       start with url
  -f FILE      load url from file
  -h --help    show this help message
"""
from docopt import docopt


def get_arguments():
    return docopt(__doc__)
