#!/usr/bin/env python

num = int(raw_input())
for z in range(num):
	dna = raw_input()
	virus = raw_input()
	blank = raw_input()
	
	if len(virus) == 0:
		print
		continue
	if len(virus) < 2:
		print "0"
		continue
	
	for start in range(len(dna)):

