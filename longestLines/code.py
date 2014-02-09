import sys
test_cases = open(sys.argv[1], 'r')
topNum = int(test_cases.readline().strip())
words = []
for test in test_cases:
  words.append(test.strip())
words = sorted(words, key=len, reverse=True)
for i in range(topNum):
  print words[i]
test_cases.close()
