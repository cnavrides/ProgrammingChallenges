#!/usr/bin/env python

cases = int(raw_input())
for case in range(cases):
  vals = raw_input().split()
  n = int(vals[0])
  m = int(vals[1])

  lawn = []
  for i in range(n):
    lawn.append([int(x) for x in raw_input().split()])
  answer = "YES"
  for row in range(n):
    for col in range(m):
      isMin  = True
      # Check if value is max of row
      for r in range(n):
        if lawn[row][col] < lawn[r][col]:
          isMin = False
          break
      if isMin:
        continue
      isMin = True
      for c in range(m):
        if lawn[row][col] < lawn[row][c]:
          isMin = False
          break
      if isMin == False:
        answer = "NO"
        break
    if answer == "NO":
      break    

  print "Case #%i: %s" % (case+1, answer)
