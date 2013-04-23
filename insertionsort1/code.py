#!/usr/bin/env python
def printVals(nums, pointer):
  tmp = ''
  for x in range(len(nums)):
    if x >= pointer + 1:
      tmp += str(nums[x-1])
    else:
      tmp += str(nums[x])
    tmp += ' '
  print tmp

tmp = int(raw_input())
numbers = raw_input().split()
nums = [int(x) for x in numbers]

moveVal = nums[-1:][0]
pointer = len(nums)-2

while moveVal <  nums[pointer]:
  printVals(nums, pointer)
  pointer -= 1

nums = sorted(nums)
tmp = '' 
for x in nums:
  tmp += str(x) + ' '

print tmp
