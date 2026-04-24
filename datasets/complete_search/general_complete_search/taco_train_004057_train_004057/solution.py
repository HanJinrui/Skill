import sys
from collections import deque
n = int(input())
(sy, sx, ey, ex) = map(int, input().split())
Q = deque()
Q.append(('', sx, sy, 0))
moves = [(-1, -2), (1, -2), (2, 0), (1, 2), (-1, 2), (-2, 0)]
name = {(-1, -2): 'UL ', (1, -2): 'UR ', (2, 0): 'R ', (1, 2): 'LR ', (-1, 2): 'LL ', (-2, 0): 'L '}
M = {}
while Q:
	(way, x, y, d) = Q.popleft()
	if x == ex and y == ey:
		print(d)
		print(way.strip())
		sys.exit(0)
	if (x, y) in M:
		continue
	M[x, y] = d
	for (dx, dy) in moves:
		if 0 <= x + dx < n and 0 <= y + dy < n:
			Q.append((way + name[dx, dy], x + dx, y + dy, d + 1))
print('Impossible')
