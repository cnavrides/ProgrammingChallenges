#!/usr/bin/env python

lines = int(raw_input())

for i in range(lines):
	line = raw_input()
	words = line.split()
	length = len(words)

	stringBuild = ""
	for j in range(length):
		stringBuild += words[length-1-j] + " "
	print "Case #" + str(i+1) + ":", stringBuild[:-1]



