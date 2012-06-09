#!/usr/bin/env python

num = int(raw_input())

for z in range(num):
	size = int(raw_input())
	v1 = []
	v2 = []
	tmp1 = raw_input().rstrip('\n').split()
	tmp2 = raw_input().rstrip('\n').split()
	for n in range(len(tmp1)):
		v1.append(int(tmp1[n]))
		v2.append(int(tmp2[n]))

	v1.sort()
	v2 = sorted(v2, reverse = True)
	x = 0 
	for i in range(len(v1)):
		x += v1[i] * v2[i]

	print "Case #" + str(z+1) + ":", x		

	
