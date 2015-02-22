# https://www.codeeval.com/open_challenges/87/
import sys
test_cases = open(sys.argv[1], 'r')
length = 256
array = [[0 for i in range(length)] for j in range(length)]

for test in test_cases:
  inLineVals = test.strip().split()
  if 'SetCol' == inLineVals[0]:
   col = int(inLineVals[1])
   val = int(inLineVals[2])
   for i in range(length):
    array[i][col] = val 

  elif 'SetRow' == inLineVals[0]:
   row = int(inLineVals[1])
   val = int(inLineVals[2])
   for i in range(length):
    array[row][i] = val


  elif 'QueryCol' == inLineVals[0]:
   col = int(inLineVals[1])
   total = 0
   for i in range(length):
    total += array[i][col]
   print total

  elif 'QueryRow' == inLineVals[0]:
   row = int(inLineVals[1])
   total = 0
   for i in range(length):
    total += array[row][i]
   print total
test_cases.close()