#!/usr/bin/env python
import sys, re

def getUpDown(xDistance):
  if xDistance > 0:
    return 'UP'
  else:
    return 'DOWN'
    
def getLeftRight(yDistance):
  if yDistance > 0:
    return 'LEFT'
  else:
    return 'RIGHT'
def next_move(posx, posy, dimx, dimy, board):
  spotLocations = [spot.start() for spot in re.finditer('d', board)]

  distances = {}
  for spot in spotLocations:
    x = spot/dimx
    y = spot%dimy

    xDistance = posx - x
    yDistance = posy - y
    move = ''
    if yDistance == 0:
      move = getUpDown(xDistance)
    elif xDistance == 0:
      move = getLeftRight(yDistance)
    elif abs(xDistance) < abs(yDistance):
      move = getUpDown(xDistance)
    else:
      move = getLeftRight(yDistance)
      
    dis = abs(x - posx) + abs(y - posy)
    if dis == 0:
      return "CLEAN"
    distances[dis] = move
  return distances[sorted(distances.keys())[0]]
  '''
  spots = []
  for spot in spotLocations:
    spots.append((spot/dimx, spot%dimy))
  '''
  
currentPosition = raw_input().strip().split()
botX = int(currentPosition[0])
botY = int(currentPosition[1])

dimensions = raw_input().strip().split()
dimX = int(dimensions[0])
dimY = int(dimensions[1])

board = ''
for z in range(dimX):
  board += raw_input().strip()


#sys.stdout.write(next_move(botX, botY, dimX, dimY, board))
print next_move(botX, botY, dimX, dimY, board)
