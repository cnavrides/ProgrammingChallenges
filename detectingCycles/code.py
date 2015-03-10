import sys

def findPattern(nums):
  for num in nums:
    if nums.count(num) > 1:
      locs = [i for i,x in enumerate(nums) if x == num]
      for location in range(len(locs)-1):
        start = locs[location]
        end = locs[location+1]
        difference = end - start
        if difference + end > len(nums):
          continue
        found = True
        for i in range(difference):
          if nums[start + i] != nums[end + i]:
            found = False
            break
        if found:
          print ' '.join(nums[start:end]).strip()
          return

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  findPattern(test.split())
test_cases.close()
