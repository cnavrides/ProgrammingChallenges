#!/usr/bin/env python
def isValid(nums):
	global daysPerMonth
	year = nums[2]
	month = nums[0]
	day = nums[1]
	#get 4 digit year
	if year < 100:
		year += 2000
	offset = 0
	if year % 4 == 0:
		if (year % 100 != 0 or year % 400 == 0) and month == 2:
			offset = 1
	
	if month > 12 or month < 1:
		return 99999999

	if day > (daysPerMonth[month -1]+offset) or day < 1:
		return 99999999
	return int(str(year) + str(month).zfill(2) + str(day).zfill(2))

daysPerMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

'''	
print isValid([0,0,1900])
print isValid([1,1,2000])
print isValid([2,29,2000])
'''

#get input
rawIn = raw_input()
x = rawIn.strip().split('/')

#store values
nums = []
for val in x:
	nums.append(int(val))

possibilities = []
for i in range(3):
	possibilities.append(isValid(nums))
	possibilities.append(isValid([nums[1],nums[0], nums[2]]))
	
	tmp = nums[0]
	nums[0] = nums[1]
	nums[1] = nums[2]
	nums[2] = tmp
s = sorted(possibilities)
if s[0] == 99999999:
	print rawIn + " is illegal" 
else:
	tmp = str(s[0])
	print tmp[:4]+"-"+tmp[4:6] +"-"+tmp[6:]

