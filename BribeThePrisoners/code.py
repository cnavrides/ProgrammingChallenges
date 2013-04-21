#!/usr/bin/env python
def bribeAmount(Array, which, offset=0, p = False):
#	if p == True:
#		print Array, which, offset
	if len(which) == 0:
		return 0
	length = len(Array) - 1
	if len(which) == 1:
		return length
	if len(Array) < 1 or len(which) < 1:
		return 0
	m = 9999999999999999
	count = 0
	#test the value based on which prisoner is released
	for w in range(len(which)):
		#cost to bribe all prisoner + cost of left + cost of right
		tmp = length +  bribeAmount(Array[:which[w]-offset], which[:w], offset) + bribeAmount(Array[which[w]+1-offset:],which[w+1:], which[w]+offset+1)
		if tmp < m:
			m = tmp
	return m 
		
cases = int(raw_input())

for z in range(cases):
	line = raw_input().split()
	cells = int(line[0])
	release = int(line[1])
	total = 0
	#0 for filled, -1 for empty, 1 for to be released
	filled = [0 for x in range(cells)]
	half = cells / 2
	which = []
	if z == 10:
		print line
	if release > 0:
		line = raw_input().split()
		if z == 10:
			print line
		for val in line:
			filled[int(val)-1] = 1
			which.append(int(val)-1)	
	
	
	total = bribeAmount(filled, which)
	
	print "Case #" + str(z+1) + ":", total
