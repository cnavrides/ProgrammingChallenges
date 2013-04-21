#!/usr/bin/env python
import sys

def displayPathtoPrincess(n, grid):
  total = ''
  for row in grid:
    total += row

  # Find the bot.
  tmp = total.find('m')
  if tmp == -1:
    print "ERROR NOT FOUND!"
    exit()
  bot = (tmp/size, tmp%size)

  # Find the princess.
  tmp = total.find('p')
  if tmp == -1:
    print "ERROR NOT FOUND!"
    exit()
  princess = (tmp/size, tmp%size)

  # Get the up or down difference
  upDown = bot[0] - princess[0]
  if upDown < 0:
    udMovement = 'DOWN'
    upDown *= -1
  else:
    udMovement = 'UP'

  # Get the left or right difference
  leftRight = bot[1] - princess[1]
  if leftRight < 0:
    lrMovement = 'RIGHT'
    leftRight *= -1
  else:
    lrMovement = 'LEFT'

  moves = ''
  # Print out how many up or downs
  while upDown > 0:
    upDown -= 1
    moves +=  udMovement + '\n'

  # Print out how many left or rights
  while leftRight > 0:
    leftRight -= 1
    moves += lrMovement + '\n'
    
  # Print the moves
  sys.stdout.write(moves)
    
# Get the size
size = int(raw_input())
# Get the total string
grid = []
for row in range(size):
  grid.append(raw_input())


displayPathtoPrincess(size,grid)