#!/usr/bin/env python
def findString(s1, s2):
	for i in range(len(s2)):
		tmp 
cases = int(raw_input())
for z in range(cases):
	s1 = raw_input()
	s2 = raw_input()
	maxLen = 0
	loc = 0
	#starting
	for i in range(len(s2)):
		tmp = ""
		#ending
		for j in range(i, len(s2)):
			tmp += s2[j]
			if tmp in s1 and len(tmp) > maxLen:
					maxLen = len(tmp)
					loc = s1.find(tmp)
	print maxLen, loc