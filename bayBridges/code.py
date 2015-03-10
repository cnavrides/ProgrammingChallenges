import sys

vals = []
nodes = []
class node:
  def __init__(self, points):
    self.a = -1
    self.points = points
    self.blockers = []
    self.called = False
    self.isAlive = True

class point:
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

# DFS search to see if this is better to remove or keep.
def getDifference(val, multiplier=1.0):
  total = multiplier
  val.called = True
  for blocker in val.blockers:
    if not vals[blocker].called and vals[blocker].isAlive:
      total += multiplier
      total += getDifference(vals[blocker], multiplier * -1)
  val.called = False
  return total

# DFS to delete the bridges deemed not necessary.
def deleteRecursive(val, deleteThis = True):
  val.called = True
  for blocker in val.blockers:
    if vals[blocker].isAlive:
      if deleteThis:
        vals[blocker].isAlive = False
      deleteRecursive(vals[blocker], False if deleteThis else True)
  val.called = False

# Check if any of the blockers are still alive.
def blockersAlive(blockers):
  for blocker in blockers:
    if vals[blocker].isAlive:
      return True
  return False

# Checks if there are blocking bridges still.
def areBlockers():
  for val in vals:
    if val.isAlive and blockersAlive(val.blockers):
      return True
  return False

# Are points A,B,C listed in counter clockwise order.
def ccw(A,B,C):
    return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

# Returns True if the two lines intersect.
def intersect(id1, id2):
  line1 = vals[id1].points
  line2 = vals[id2].points
  x1 = line1[0][0]
  y1 = line1[0][1]
  x2 = line1[1][0]
  y2 = line1[1][1]

  x3 = line2[0][0]
  y3 = line2[0][1]
  x4 = line2[1][0]
  y4 = line2[1][1]

  A = point(x1, y1)
  B = point(x2, y2)
  C = point(x3, y3)
  D = point(x4, y4)
  return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


def main(argv=None):
  test_cases = open(sys.argv[1], 'r')

  for test in test_cases:
    vals.append(node(eval(test.strip().split(': ')[1])))

  for i in range(len(vals)-1):
    for j in range(i+1, len(vals)):
      if intersect(i, j):
        vals[i].blockers.append(j)
        vals[j].blockers.append(i)

  while(areBlockers()):
    for val in vals:
      if val.isAlive and blockersAlive(val.blockers):
        if getDifference(val) > 0:
          deleteRecursive(val, False)
        else:
          deleteRecursive(val, True)

  for i in range(len(vals)):
    if vals[i].isAlive:
      print i+1


  test_cases.close()
if __name__ == "__main__":
  sys.exit(main())
