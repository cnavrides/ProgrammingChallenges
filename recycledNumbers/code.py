#!/usr/bin/env python

cases = int(raw_input())
for c in range(cases):
	line = (raw_input()).rstrip('\n').split()
	a = int(line[0])
	b = int(line[1])
	count = 0
	found = {}
	for num in range(a,b):
#		if num % 10 == 0 or num < 12:
#			continue
#		if num in found:
#			continue
		strNum = str(num)
		for i in range(1, len(strNum)):
			tmpStr = strNum[i:] + strNum[:i]
			if tmpStr == strNum:
				break
#			if tmpStr[0] == '0':
#				continue
			tmpNum = int(tmpStr)

			if a <= tmpNum  <= b :
#				found[tmpNum] = 1
				if num < tmpNum:
					tStr = str(num) + str(tmpNum)
				else:
					tStr = str(tmpNum) + str(num)
				if not tStr in found:
					found[tStr] = 1
	print "Case #"+str(c+1) + ":", len(found)
