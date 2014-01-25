#!/usr/bin/python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from functools import wraps
#memory function that stores values in recursive function 
def memo(func):
	cache = {}
	@wraps(func)
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap
#recursively add to answer list
def findStrings(currentString):
        global  H, m
	if currentString == m:
		return 0 
	count = 0
	for s in H:
		temp = currentString + len(s) 
                if temp <= m:
                        count += findStrings(temp) + 1
	return count

def isSuper(currentString):
    lessThan = False
    letters = ['a','b','c','d','e','f','g','h','i' ,'j']
    if len(currentString) == 1:
		return currentString in letters
    if currentString[len(currentString)-1] not in letters:
            return False
    for i in range(len(currentString) - 1):
            if currentString[i] not in letters:
                   return False
            if not lessThan:
                for j in range(i+1, len(currentString)):
                        if currentString[i] < currentString[j]:
       	        		lessThan = True
				break
	    return lessThan

findStrings = memo(findStrings)

data = sys.stdin.readlines()

H = []
n = m = -1
first = True
count = 0
for line in data:
        if first:
            first = False
            n = int(line.strip().split()[0])
            m = int(line.strip().split()[1])
            continue
     	count  += 1
#	if count > n:
#		break
#   	if len(line.strip()) > m:
#                continue
#	if isSuper(line.strip()):
       	H.append(line.strip())
H = set(H)

print (findStrings(0)+1) % 1000000007

