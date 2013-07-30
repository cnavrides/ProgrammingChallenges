#!/usr/bin/env python
import math
cases = int(raw_input())
for case in range(cases):
	line = raw_input().split()
	radius = int(line[0])
	paint = int(line[1])
	rings = 0

	while True:
		nextArea = radius * 2 + 1
		#nextArea = (radius + 1) ** 2 - radius ** 2
		if nextArea <= paint:
			paint -= nextArea
			rings += 1
			radius += 2
			#print "paint:", paint, "next Area:", nextArea
		else:
			#print "nextArea:", nextArea
			break

	print "Case #%i: %i" % (case+1, rings)
	
