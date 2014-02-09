import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  fNum = int(test.strip())
  if fNum == 0:
    print 0
    continue
  fOne = 1
  fTwo = 1
  count = 2
  while count < fNum:
    tmp = fTwo + fOne
    fOne = fTwo
    fTwo = tmp
    count += 1
  print fTwo
test_cases.close()