#!/usr/bin/python
import sys

filename = '../../Program.cs'

with open(filename) as f:
    newText=f.read().replace('{commit}', sys.argv[0])

with open(filename, "w") as f:
    f.write(newText)
