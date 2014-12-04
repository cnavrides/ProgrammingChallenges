#!/usr/bin/env python
import sys

inFileName = sys.argv[1]

with open(inFileName) as inFile:
  lines = inFile.readlines()
  for l in lines:
    line = l.strip()
    parts = line.split(' ')
    num = int(parts[-1:][0])
    if num <= len(parts)-1:
      parts = parts[0:(len(parts)-1)]
      print parts[num%len(parts)]
    else:
      parts[0]