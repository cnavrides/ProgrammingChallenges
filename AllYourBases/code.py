#!/usr/bin/env python

charOffset = 87
intOffset = 48

cases = int(raw_input())
#because the language can't start with 0
vals = ['1', '0']
#add the int vals
for i in range(2,10):
	vals.append(chr(intOffset+i))
#add the char values
for i in range(26):
	vals.append(chr(charOffset+i+10))

#go through the cases
for z in range(cases):
	maxVal = 0
	inLine = raw_input()
	
	line = ""
	count = 0
	charSet = {}
	#find the minimum string
	for c in inLine:
		if not c in charSet:
			charSet[c] = vals[count]
			count += 1
		line += charSet[c]
		
	#reverse a string
	line = line[::-1]
	
	#get the base
	for c in line:
		if ord(c) < 90:
			num = ord(c) - intOffset
		else:
			num = ord(c) - charOffset
		if num > maxVal:
			maxVal = num
	base = maxVal + 1
	total = 0
	count = 0
	#find the total
	for c in line:
		if ord(c) < 90:
			num = ord(c) - intOffset
		else:
			num = ord(c) - charOffset
			
		total += num * (base ** count)
		count += 1
	print "Case #" + str(z+1) + ":", total
