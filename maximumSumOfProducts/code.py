#!/usr/bin/env python

cases = int(raw_input())

for z in range(cases):
	num = int(raw_input())
	n = [-1 for i in range(num)]
	middle = num/2
	offset = 0
	if num % 2 != 0:
		n[middle] = num
		num -= 1
	else:
		offset = 1
	for i in range(1,middle+1):
		n[middle+i-offset] = num
		num -= 1
		
		n[middle-i] = num
		num -= 1
	total = 0
	for i in range(len(n)-1):
		total += n[i] * n[i+1]
		
	print total