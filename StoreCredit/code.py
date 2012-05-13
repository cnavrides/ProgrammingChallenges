#!/usr/bin/env python

cases = int(raw_input())

for i in range(cases):
	credit = int(raw_input())
	items = int(raw_input())
	data = raw_input().split()
	values = []
	originalLocation = {}
	for j in range(items):
		tmp = int(data[j])
		values.append(tmp)
		if tmp in originalLocation:
			originalLocation[tmp].append(j+1)
		else:
			originalLocation[tmp] = [j+1]
	values = sorted(values)
	a = 0
	b = items-1
	total = values[a] + values[b]
	while total != credit:
		if total > credit: 
			b -= 1
		else:
			a += 1
		total = values[a] + values[b]
	aVal = values[a]
	bVal = values[b]
	if originalLocation[aVal][0] > originalLocation[bVal][0]:
		second = originalLocation[aVal].pop()
		first = originalLocation[bVal].pop()
	else:
		second = originalLocation[bVal].pop()
		first = originalLocation[aVal].pop()
	print "Case #" + str(i+1) + ":", first, second
	
	

