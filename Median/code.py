#!/usr/bin/env python
import bisect
N = int(raw_input())
l = 0
nums = []
ms = ''
for z in range(N):
	vals = raw_input().split()
	if vals[0] == 'r':
		if int(vals[1]) in nums:
			nums.remove(int(vals[1]))
			l -= 1
			if l == 0:
				print "Wrong!"
			else:
				if l % 2 == 0:
					print '%.1f' %((nums[l/2]+nums[l/2-1])/2.0)
				else:
					print str(nums[l/2]) 
		else:
			print  "Wrong!"
	else:
		bisect.insort(nums, int(vals[1]))
		l+=1
		if l % 2 == 0:
			print '%.1f' %((nums[l/2]+nums[l/2-1])/2.0)
		else:
			print str(nums[l/2])

