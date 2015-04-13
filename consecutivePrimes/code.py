import sys
import itertools

test_cases = open(sys.argv[1], 'r')
found = {}

def isPrime(num):
  for i in xrange(2,num/2):
    if num%i == 0:
      return False
  return True

def checkUnique(necklace):
  necklace_string = ''.join(str(x) for x in necklace)
  if necklace_string in found:
    return 
  for i in range(len(necklace)):
    key = necklace_string[-i:] + necklace_string[:-i]
    found[key] = True

def generateNecklace(current, available, level = 0):
  options = list(available)
  if len(available) == 0:
    if isPrime(current[0] + current[-1]):
      checkUnique(current)
    return
  elif len(current) == 0:
    for i in options:
      available.remove(i)
      generateNecklace(current+[i], list(available), level+1)
      available.append(i)
  else:
    for i in options:
      if isPrime(current[-1] + i):
        available.remove(i)
        generateNecklace(current + [i], list(available), level + 1)
        available.append(i)
  
for test in test_cases:
  found = {}
  val = int(test.strip())
  necklace = [i+1 for i in range(val)]
  generateNecklace([], necklace)
  print len(found.keys())/val

test_cases.close()
