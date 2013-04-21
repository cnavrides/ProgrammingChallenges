#!/usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUTn,
n,k = raw_input().split()
if n == '0':
  print '0'
  exit()

k = int(k)
allNumbers = dict( (int(num), True) for num in raw_input().split())

count = 0
for n in allNumbers:
  if (n+k) in allNumbers:
    count += 1

print count
