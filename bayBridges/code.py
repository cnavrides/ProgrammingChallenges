import sys

vals = []
nodes = []
class node:
  def __init__(self, points):
    self.points = points
    self.blockers = []
    self.called = False
    self.isAlive = True


# recursively turn on/off
def getDifference(val, multiplier=1.0):
  total = multiplier
  val.called = True
  for blocker in val.blockers:
    if not vals[blocker].called and vals[blocker].isAlive:
      total += multiplier
      total += getDifference(vals[blocker], multiplier * -1)
  val.called = False
  return total

def deleteRecursive(val, deleteThis = True):
  val.called = True
  for blocker in val.blockers:
    if not vals[blocker].called and vals[blocker].isAlive:
      if deleteThis:
        val.isAlive = False
      deleteRecursive(vals[blocker], False if deleteThis else True)
  val.called = False


def blockersAlive(blockers):
  for blocker in blockers:
    print 'blockerAlive:', blocker, vals[blocker].isAlive
    if vals[blocker].isAlive:
      return True
  return False

def areBlockers():
  count = 0
  for val in vals:

    if val.isAlive and blockersAlive(val.blockers):
      print count, 'areBlockers: ', val.isAlive, val.blockers
      return True
    count += 1
  return False

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

  l1_x = x2 - x1
  l1_y = y2 - y1

  l2_x = x3 - x4
  l2_y = y3 - y4
  s = (-l1_y * (x1 - x3) + l1_x * (y1 - y3)) / (-l2_x * l1_y + l1_x * l2_y)
  t = ( l2_x * (y1 - y3) - l2_y * (x1 - x3)) / (-l2_x * l1_y + l1_x * l2_y)
  if s >= 0 and s <= 1 and t >= 0 and t <= 1:
    return True
  return False
  '''
{
    float s1_x, s1_y, s2_x, s2_y;
    s1_x = p1_x - p0_x;     s1_y = p1_y - p0_y;
    s2_x = p3_x - p2_x;     s2_y = p3_y - p2_y;

    float s, t;
    s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y);
    t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y);

    if (s >= 0 && s <= 1 && t >= 0 && t <= 1)
    {
        // Collision detected
        if (i_x != NULL)
            *i_x = p0_x + (t * s1_x);
        if (i_y != NULL)
            *i_y = p0_y + (t * s1_y);
        return 1;
    }

    return 0; // No collision
  '''
  x12 = x1 - x2;
  x34 = x3 - x4;
  y12 = y1 - y2;
  y34 = y3 - y4;

  c = x12 * y34 - y12 * x34;

  if abs(c) < 0.01:
    return False
  return True

def main(argv=None):
  test_cases = open(sys.argv[1], 'r')

  for test in test_cases:
    vals.append(node(eval(test.strip().split(': ')[1])))

  for i in range(len(vals)-1):
    for j in range(i+1, len(vals)):
      if intersect(i, j):
        print "INTERSECT"
        print "      ", vals[i].points
        print "      ", vals[j].points
        vals[i].blockers.append(j)
        vals[j].blockers.append(i)
  count = 0
  for val in vals:
    print count, val.blockers
    count += 1
  '''
  while(areBlockers()):
    for val in vals:
      if val.isAlive and blockersAlive(val.blockers):
        if getDifference(val) > 0:
          deleteRecursive(val, False)
        else:
          deleteRecursive(val, True)

  for i in range(len(vals)):
    if val.isAlive:
      print i+1
  '''

  test_cases.close()
if __name__ == "__main__":
  sys.exit(main())
