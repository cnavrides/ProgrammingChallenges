#!/usr/bin/env python
vowels = ['a', 'e', 'i', 'o', 'u']
num = int(raw_input().rstrip('\n'))

for i in range(num):
	name = raw_input().rstrip('\n')
	lastChar = name[len(name)-1].lower()
	if lastChar in vowels:
		who = "a queen"
	elif lastChar == 'y':
		who = "nobody"
	else:
		who = "a king"
	
	print "Case #" + str(i+1) + ": " + name + " is ruled by " + who + "."

