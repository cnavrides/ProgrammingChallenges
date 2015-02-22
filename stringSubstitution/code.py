import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  current = test.split(';')[0]
  swaps = test.strip().split(';')[1].split(',')
  pieces = {}
  for i in range(len(swaps)/2):
    key = 'x' + str(i+2)
    current = current.replace(swaps[i*2], key)
    pieces[key]= swaps[i*2 + 1]
  for piece in pieces:
    current = current.replace(piece, pieces[piece])
  print current
test_cases.close()
