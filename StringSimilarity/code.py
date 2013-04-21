#!/usr/bin/env python

lines = int(raw_input())
for i in range(lines):
	S = raw_input()
	tmp = S
	count = 0
	for i in range(len(S)):
		for loc in range(len(tmp)):
			if tmp[loc] == S[loc]:
				count += 1
			else:
				break
		tmp = tmp[1:]
	print count


