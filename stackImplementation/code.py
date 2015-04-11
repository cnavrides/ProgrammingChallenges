import sys

class stack:
  def __init__(self):
    self.vals = []

  def push(self, val):
    self.vals.append(val)

  def pop(self):
    if len(self.vals) == 0:
      return None
    tmp = self.vals[-1]
    self.vals = self.vals[:-1]
    return tmp
  
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
  output = ''
  nums = test.strip().split()
  my_stack = stack()
  for num in nums:
    my_stack.push(num)
  
  while True:
    tmp = my_stack.pop()
    if tmp == None:
      break
    output += tmp + ' '
    if my_stack.pop() == None:
      break

  print output[:-1]
test_cases.close()
