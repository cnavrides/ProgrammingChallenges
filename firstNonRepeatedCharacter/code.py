import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  test = test.strip()
  for letter in test:
    if test.count(letter) == 1:
      print letter
      break
test_cases.close()
