#!/usr/bin/env python
import sys

inFileName = sys.argv[1]

with open(inFileName) as inFile:
	lines = inFile.readlines()
	for l in lines:
		line = l.strip()
		count = 0
		isSelfDescribing = True
		for char in line:
			if line.count(str(count)) != int(char):
				isSelfDescribing = False
				break
			count += 1
		if isSelfDescribing:
			print 1
		else:
			print 0
