#!/usr/bin/env python
def getOther(left, right):
	if 'a' != left and 'a' != right:
		return 'a'
	elif 'b' != left and 'b' != right:
		return 'b'
	return 'c'

cases = int(raw_input())

for z in range(cases):
	line = raw_input()
	count = 0
	length = len(line) - 1 
	while count < length:
		if line[count] != line[count+1]:
			line = line[:count] + getOther(line[count], line[count+1]) + line[count+2:]
			length -= 1
			
			if count > 0:
				count -= 1
		else:
			count += 1

	print len(line)
