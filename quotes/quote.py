#! /usr/bin/python

import random
import sys
import textwrap
import os

QUOTEPATH = os.path.dirname(os.path.abspath(sys.argv[0])) + "/../etc/quotes.txt"
WRAPLEN = 80

quotefile = open(QUOTEPATH, "r")

lines = quotefile.readlines()

linenum = random.randint(0, len(lines)-1)

actline = 0
for line in lines:
    if actline == linenum:
        wrappedlines = textwrap.wrap(line, WRAPLEN)
        for wrappedline in wrappedlines:
            print(wrappedline)
        break
    else:
        actline += 1
