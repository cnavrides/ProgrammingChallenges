#!/usr/bin/env python
class node:
	def __init__(self, i):
		self.val = i
		self.who = []
	
cases = int(raw_input())
for z in range(cases):
		n,d = raw_input().split()
		n = int(n)
		d = int(d)
		
		val = {}
		known = {}
		#graph
		g = [node(i) for i in range(n)]
		for i in range(n-1):
			a, b = raw_input().split()
			a = int(a)
			b = int(b)
			g[a].who.append(b)
			g[b].who.append(a)
			
		for z in range(len(g)):
			val[z] = len(g[z].who)
		print val
		blankLine = raw_input()
			