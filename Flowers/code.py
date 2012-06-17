#!/usr/bin/env python
# code snippet illustrating input/output methods 
N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
	C.append( int(number) )
	i = i+1

result = 0
#sort so highest value is first
C = sorted(C, reverse=True)
num = [0 for i in range(K)]

count = 0
for i in range(N):
	result += (num[i%K] + 1) * C[i]
	num[i%K] += 1
print result
