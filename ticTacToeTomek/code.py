#!/usr/bin/env python
def checkRows(board):
  for row in board:
    if '.' not in row and ('X' not in row or 'O' not in row):
      if 'X' in row:
        return True, 'X'
      elif 'O' in row:
        return True, 'O'
      else:
        return True, 'T'
  return False, None

def checkColumns(board):
  # Rotate board. Call checkRows.
  rotatedBoard = ['' for x in range(len(board))]
  for row in board:
    for x in range(len(row)):
      rotatedBoard[x] += row[x]
  return checkRows(rotatedBoard)

def checkDiaganols(board):
  top = ''
  bottom = '' 
  # Build strings for  TL -> BR & BL -> TR
  for i in range(len(board)):
    top += board[i][i]
    bottom += board[len(board)-i-1][i]

  # Check the top left to bottom right
  if '.' not in top and ('X' not in top or 'O' not in top):
    if 'X' in top:
      return True, 'X'
    elif 'O' in top:
      return True, 'O'
    else:
      return True, 'T'
  
  # Check the bottom left to top right  
  if '.' not in bottom and ('X' not in bottom or 'O' not in bottom):
    if 'X' in bottom:
      return True, 'X'
    elif 'O' in bottom:
      return True, 'O'
    else:
      return True, 'T'

  # Return no match found
  return False, None 
  

# Check if the board has not completed.
def checkNotCompleted(board):
  for row in board:
    if '.' in row:
      return True
  return False

# Print the winner
def winner(game, winner):
  print "Case #%i: %s won" % (game+1, winner)

board_size = 4

numGames = int(raw_input())

for game in range(numGames):
  board = []
  # Fill in the board
  for i in range(board_size):
    board.append(raw_input())
  # Clear the line inbetween, but don't crash if there is no extra last line
  try:
    tmp = raw_input()
  except:
    tmp = ''

  # Check each row
  found, player = checkRows(board)
  if found:
    winner(game, player)
    continue

  # Check each column
  found, player = checkColumns(board)
  if found:
    winner(game, player)
    continue

  # Check Diaganol
  found, player = checkDiaganols(board)
  if found:
    winner(game, player)
    continue

  # Check not completed
  if checkNotCompleted(board):
    print "Case #%i: Game has not completed" % (game+1)
    continue

  # Print out it was a tie
  print "Case #%i: Draw" % (game+1)
