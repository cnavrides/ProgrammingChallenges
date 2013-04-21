#!/usr/bin/env python
import operator
from operator import itemgetter, attrgetter
cases = int(raw_input())
for z in range(cases):
	numLvls = int(raw_input())
	times = raw_input().split()

	percent = raw_input().split()
	
	#sort based upon hardest first
	count = 0
	order = []
	for p in percent:
		order.append( (float(percent[count]) * float(times[count]), count))
		count +=1
	sList = sorted(order, key=itemgetter(0), reverse=True)	
		
	answer = ""
	for n in sList:
		answer += str(n[1]) + " "
	print "Case #" + str(z+1) + ": " + answer[:-1]
