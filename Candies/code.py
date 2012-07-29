#!/usr/bin/env python
N = int(raw_input())

kid = []
candy = []
val = []
#get values in
for x in range(N):
	kid.append(int(raw_input()))
	candy.append([])
	val.append(-1)
#get if smaller than 3 students
if N < 3:
	if N == 1:
		print 1
		exit()
	else:
		if kid[0] == kid[1]:
			print 2
			exit()
		else:
			print 3
			exit()
total = 0
#get endings
if kid[0] > kid[1]:
	candy[0] = [1]

if kid[N-1] > kid[N-2]:
	candy[N-1] = [N-2]

'''
Go through and find where each student has a higher score than 
someone sitting next to them
'''
for k in range(1, N-1):
	if kid[k] > kid[k-1]:
		candy[k].append(k-1)
	if kid[k] > kid[k+1]:
		candy[k].append(k+1)
#get all the values where it is just1 candy
for x in range(N):
	if len(candy[x]) == 0:
		val[x] = 1
		total += 1
#go through L -> R and assign values
for x in range(N):
	if len(candy[x]) == 1:
		if candy[x][0] < x:
			val[x] = val[x-1]+1
			total += val[x]
#go through R -> L and assing values
for y in range(N):
	x = N-1-y
	if len(candy[x])== 1:
		if candy[x][0] > x:
			val[x] = val[x+1]+1
			total += val[x]
#get all the values where they are higher than both students
for x in range(N):
	if len(candy[x]) == 2:
		if val[candy[x][0]] > val[candy[x][1]]:
			val[x] = val[candy[x][0]]+1
			total += val[x]
		else:
			val[x] = val[candy[x][1]]+1
			total += val[x]
#print total
print total
