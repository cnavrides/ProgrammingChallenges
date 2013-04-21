#!/usr/bin/env python
import math
cases = int(raw_input())
for z in range(cases):
	line = raw_input().split()
	l = int(line[0])
	p = int(line[1])
	c = int(line[2])
	count = 0
	
	current = l * c
	nums = []
	if current < p:
		nums.append(current)
	while current < p:
		current = current * c
		nums.append(current)

	if len(nums) > 0:
		nums.pop()
	length = len(nums)
	if length % 2 == 0 and length != 0:
		count += 1
	if length > 0:
		count += int(math.ceil(math.log(length, c)))	
	
	print "Case #" + str(z+1) + ":", count
