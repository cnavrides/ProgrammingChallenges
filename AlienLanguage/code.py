#!/usr/bin/env python
import re

info = raw_input().split()
l = int(info[0])
d = int(info[1])
n = int(info[2])

knownWords = []
#words
for i in range(d):
	knownWords.append(raw_input())
	
#test cases
for num in range(n):
	line = raw_input()
	myStr = line.replace("(","[").replace(")","]")
	#get all the strings possible then return the ones also in knownWords
	foundWords = filter(re.compile(myStr).search, knownWords)
	print "Case #" + str(num+1) + ":", len(foundWords)
