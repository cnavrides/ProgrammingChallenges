#!/usr/bin/env python
import sys

def nextMove(n,x,y,grid):
  total = ''
  for row in grid:
    total += row

  # Find the princess.
  tmp = total.find('p')
  if tmp == -1:
    print "ERROR NOT FOUND!"
    exit()
  princess = (tmp/size, tmp%size)

  # Get the up or down difference
  upDown = x - princess[0]
  if upDown < 0:
    udMovement = 'DOWN'
    upDown *= -1
  else:
    udMovement = 'UP'

  # Get the left or right difference
  leftRight = y - princess[1]
  if leftRight < 0:
    lrMovement = 'RIGHT'
    leftRight *= -1
  else:
    lrMovement = 'LEFT'

  # Print out how many up or downs
  if upDown > 0:
    return (udMovement)

  # Print out how many left or rights
  if leftRight > 0:
    return(lrMovement)
    
  return ""
    
# Get the size
size = int(raw_input())
bot = raw_input().split()
x = int(bot[0])
y = int(bot[1])
# Get the total string
grid = []
for row in range(size):
  grid.append(raw_input())


# Print the moves
sys.stdout.write(nextMove(size,x,y,grid))