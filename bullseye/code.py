#!/usr/bin/env python
import math
cases = int(raw_input())
for case in range(cases):
	line = raw_input().split()
	radius = int(line[0])
	paint = int(line[1])
	rings = 0

	while True:
		nextArea = math.pi * ((radius + 1) ** 2 - radius ** 2)
		if nextArea < paint:
			paint -= nextArea
			rings += 1
		else:
			break

	print rings
	
