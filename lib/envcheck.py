# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/FileSensor
# author = i@cdxy.me

"""
Use as 'import envcheck'
It has to be the first non-standard import before your project enter main() function
"""

import sys

PYVERSION = sys.version.split()[0]

if PYVERSION < "3":
    exit("[CRITICAL] incompatible Python version detected ('%s'). "
         "For successfully running this project, you'll have to use version 3.x"
         % PYVERSION)

extensions = ("scrapy", "docopt")
try:
    for _ in extensions:
        __import__(_)
except ImportError:
    errMsg = "[CRITICAL] missing one or more requirements (%s) " % (", ".join("'%s'" % _ for _ in extensions))
    errMsg += "please run \"pip3 install -r requirements.txt\" "
    exit(errMsg)
