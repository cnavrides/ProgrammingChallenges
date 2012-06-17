#!/usr/bin/env python
#rotates and returns the new board
def rotate(board):
	l = len(board)
	tmp = [['.' for j in range(l)] for i in range(l)]
	count = 0
	for a in board:
		for b in a:
			row = (count % l)
			col = l - 1 - (count/l)
			tmp[row][col] = b
			count += 1
		
	return tmp
#will make all the pieces fall
def gravity(board):
	l = len(board)
	for col in range(l):
		for i in range(l):
			for j in range(l-1):
				row = l-j-1
				if board[row][col] == '.':
					board[row][col] = board[row-1][col]
					board[row-1][col] = '.'
	return board
	

#will return who wins in the given board.
#can reduce to less code but would rather work on other problems
def check(board, k):
	winners = []
	l = len(board)
	count = 1
	piece = ''
	#row
	for row in range(l):
		for col in range(l):
			p = board[row][col]
			if p == piece:
				count += 1 
			else:
				if count >= k and piece != '.' and not piece in winners:
					winners.append(piece)
				count = 1
				piece = p

		if count >= k and piece != '.' and not piece in winners:
			winners.append(piece)
		
		count = 1
		piece = ''
	#col
	for col in range(l):
		for row in range(l):
			p = board[row][col]
			if p == piece:
				count += 1 
			else:
				if count >= k and piece != '.' and not piece in winners:
					winners.append(piece)
				count = 1
				piece = p
		if count >= k and piece != '.' and not piece in winners:
			winners.append(piece)
		count = 1
		piece = ''
	#LR Diag
	for row in range(l-k+1):
		for col in range(l-k+1):
			for offset in range(k):
				p = board[row+offset][col+offset]
				if p == piece:
					count += 1 
				else:
					if count >= k and piece != '.' and not piece in winners:
						winners.append(piece)
					count = 1
					piece = p
			if count >= k and piece != '.' and not piece in winners:
				winners.append(piece)	

			count = 1
			piece = ''
	
	#RL Diag
	for row in range(l-k+1):
		for col in range(l-k+1):
			for offset in range(k):
				p = board[l - 1 - row-offset][col+offset]
				if p == piece:
					count += 1 
				else:
					if count >= k and piece != '.' and not piece in winners:
						winners.append(piece)
					count = 1
					piece = p
			if count >= k and piece != '.' and not piece in winners:
				winners.append(piece)	

			count = 1
			piece = ''


	if len(winners) == 0:
		return "Neither"
	if len(winners) == 2:
		return "Both"
	
	if winners[0] == 'R':
		return "Red"
	return "Blue"

#go through all the cases
cases = int(raw_input())
for z in range(cases):
	who = ""
	n,k = raw_input().split()
	board = []
	#get all the rows of the board
	for i in range(int(n)):
		tmp = raw_input()
		tmpBoard = []
		for t in tmp:
			tmpBoard.append(t)
		board.append(tmpBoard)
	#rotate the board
	board = rotate(board)
	#drop all the pieces
	board = gravity(board)
	
	#print the case and who won
	print "Case #" + str(z+1) + ":", check(board, int(k))
