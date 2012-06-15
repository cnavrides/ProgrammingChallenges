#!/usr/bin/env python
#returns a list of directories based upon the string passed in
def getDirs(dirName):
	subDirs = []
	newName = dirName[1:].split('/')
	tmp = ""
	for n in newName:
		if n == '':
			continue
		tmp +="/" + n
		subDirs.append(tmp)
	return subDirs

cases = int(raw_input())
count = 0
for z in range(cases):
	n,m = raw_input().split()	
	known = []
	for i in range(int(n)):
		tmp = getDirs(raw_input())
		for t in tmp:
			known.append(t)
	total = 0
	for i in range(int(m)):
		tmp = getDirs(raw_input())
		for t in tmp:
			if not t in known:
				total += 1
			known.append(t)
	print "Case #" + str(z+1) + ":", total
