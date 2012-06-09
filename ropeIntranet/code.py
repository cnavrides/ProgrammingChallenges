#!/usr/bin/env python

cases = int(raw_input())

for z in range(cases):
	#get the number of points
	points = int(raw_input())
	p = {}
	#store the points as tuples with key of x, for sorting reasons
	for y in range(points):
		tmp = raw_input().split()
		l = int(tmp[0])
		r = int(tmp[1])
		p[l] = (l,r)
	
	#sorted list of the keys
	vals = sorted(p)
	#store length for efficiency
	length = len(vals)
	#number of intersections
	count = 0
	
	#go through all lines
	for i in range(length):
		#get the tupple
		line = p[vals[i]]
		#get the y val
		y = line[1]
		#skip straight lines
		if line[0] == y:
			continue
		#get if line is going up or down
		if y > line[0]:
			#go through remaining lines
			for j in range(i, length):
				tmpY = p[vals[j]][1]
				#if line is going up
				if tmpY < y:
					count += 1
		else:
			for j in range(i):
				tmpY = p[vals[j]][1]
				#if it is going down, only count straight lines
				if tmpY > y and tmpY <= p[vals[j]][0]:
					count += 1
	#print results
	print "Case #" + str(z+1) + ":", count
