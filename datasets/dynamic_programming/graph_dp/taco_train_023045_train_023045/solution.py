#!/usr/bin/env python

import sys

def trymove(movegrid, x, y, num, grid):
	if x < 0 or y < 0 or x >= rows or y >= cols:
		return False
	timeleft = num - grid[x][y]
	if timeleft > movegrid[x][y]:
		movegrid[x][y] = timeleft
		return True
		#print movegrid, x, y, num

def rescue(movegrid, grid):
	progress = False
	for row in range(rows):
		for col in range(cols):
			num = movegrid[row][col]
			if num >= 0:
				if trymove(movegrid, row, col+1, num, grid) or trymove(movegrid, row+1, col, num, grid) or trymove(movegrid, row-1, col, num, grid) or trymove(movegrid, row, col-1, num, grid):
					progress = True

	if progress:
		rescue(movegrid, grid)
			#outgrid += str(grid[row][col]) + ' '
		#outgrid += '\n'
	#print outgrid

	#print rows
	#print cols
	#print movegrid
	#print grid
	#print castle

cases = sys.stdin.readline()
t = int(cases)
for p in range(t):
	inputdata = sys.stdin.readline().strip().split(' ')
	rows = int(inputdata[0])
	cols = int(inputdata[1])
	grid = []
	timegrid = []
	for row in range(rows):
		inputdata = sys.stdin.readline().strip().split(' ')
		times = list(map(int, inputdata))
		grid += [times]
		timegrid += [[-1] * len(times)]
	inputdata = sys.stdin.readline().strip().split(' ')
	castle = list(map(int, inputdata))
	time = castle.pop()
	timegrid[0][0] = time - grid[0][0]
	rescue(timegrid, grid)
	#outgrid = ''
	#for row in xrange(rows):
		#for col in xrange(cols):
			#outgrid += str(timegrid[row][col]) + ' '
		#outgrid += '\n'
	#print outgrid

	endtime = timegrid[castle[0]-1][castle[1]-1]
	if endtime >= 0:
		print('YES')
		print(endtime)
	else:
		print('NO')
