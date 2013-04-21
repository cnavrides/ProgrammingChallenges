#!/usr/bin/env python
import sys

# Get the size
size = int(raw_input())

# Get the total string
total = ''
for row in range(size):
  total += raw_input()

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

sys.stdout.write(moves)

