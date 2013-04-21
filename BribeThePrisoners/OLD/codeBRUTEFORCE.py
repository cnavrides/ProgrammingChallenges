#!/usr/bin/env python
import math
ZZZ = 0
YYY = []
def bribeAmount(Array, printMe = False):
	middle = len(Array)/2
	maxLength = middle
	maxVal = -1
	topLength = bottomLength = topVal = bottomVal = -1
	notFound = True
	top = bottom = 0
	for i in range(middle,len(Array)):
		if Array[i] == 1:
			if notFound:
				notFound = False
				topLength = i - middle
				topVal = i
				break
			top += 1	
	notFound = True
	for i in range(middle):
		if Array[middle-i-1] == 1:
			if notFound:
				notFound = False
				bottomLength = middle-i-1
				bottomVal = middle - i - 1
				break
			bottom += 1
	


	#BRUTE FORCE METHOD
	global ZZZ
		
	locations = []
	for i in range(len(Array)):
		if Array[i] == 1:
			locations.append(i)
	if len(locations) == 0:
		return 0
	maxCost = 9999999999999999
	#print locations
	for l in locations:
		maxVal = l
		tmp = len(Array) - 1 + bribeAmount(Array[:maxVal]) + bribeAmount(Array[maxVal+1:])
		#print "tmp", tmp
		if tmp < maxCost:
			maxCost = tmp
			low = l

	if printMe and (ZZZ == 17 or ZZZ == 16):
		print "      ", low, len(Array) 
		www = bribeAmount(Array[:maxVal], True) + bribeAmount(Array[maxVal+1:], True)
		#YYY.append(low)
	return maxCost


	'''	
	if topLength == bottomLength:
		if top > bottom:
			maxVal = topVal
		else:
			maxVal == bottomVal
	elif topLength > bottomLength:
		maxVal = topVal
	else:	
		maxVal = bottomVal
	
	'''	
	if topVal == bottomVal:
		return 0
	
	topCost = bottomCost = 9999999999999
	if topLength > -1:
		maxVal = topVal
		topCost = len(Array) - 1 + bribeAmount(Array[:maxVal]) + bribeAmount(Array[maxVal+1:])
	if bottomLength > -1:
		maxVal = bottomVal
		bottomCost = len(Array) - 1 + bribeAmount(Array[:maxVal]) + bribeAmount(Array[maxVal+1:])
	
	#print topCost, bottomCost
		
	if topCost > bottomCost:
		return bottomCost
	else:
		return topCost
	return len(Array) - 1 + bribeAmount(Array[:maxVal]) + bribeAmount(Array[maxVal+1:])

cases = int(raw_input())

for z in range(cases):
	line = raw_input().split()
	cells = int(line[0])
	release = int(line[1])
	total = 0
	#0 for filled, -1 for empty, 1 for to be released
	filled = [0 for x in range(cells)]
	half = cells / 2
	if release > 0:
		line = raw_input().split()
		for val in line:
			filled[int(val)-1] = 1
	
	ZZZ = z
	if ZZZ == 16 or ZZZ == 17:
		print
		print line
		print filled	
		YYY = []
		total = bribeAmount(filled, True)
		print YYY
		print "Case #" + str(z+1) + ":", total
