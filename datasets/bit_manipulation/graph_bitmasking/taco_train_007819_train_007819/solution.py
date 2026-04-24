import sys
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from collections import deque
LANS = []
t = int(input())
for tests in range(t):
	(n, m) = map(int, input().split())
	EDGE = [list(map(int, input().split())) for i in range(n - 1)]
	ELF = [list(map(int, input().split())) for i in range(m)]
	E = [[] for i in range(n + 1)]
	NODES = [-1] * (n + 1)
	NODES[1] = 0
	for (x, y, c) in EDGE:
		if c != -1:
			sc = 0
			while c != 0:
				if c % 2 == 1:
					sc += 1
				c //= 2
			c = sc % 2
		E[x].append((y, c))
		E[y].append((x, c))
	for (x, y, c) in ELF:
		E[x].append((y, c))
		E[y].append((x, c))
	Q = deque([1])
	flag = 1
	while Q and flag == 1:
		x = Q.popleft()
		if NODES[x] == -1:
			NODES[x] = 1
		for (to, c) in E[x]:
			if c != -1:
				if NODES[to] == -1:
					NODES[to] = NODES[x] ^ c
					Q.appendleft(to)
				elif NODES[to] == NODES[x] ^ c:
					True
				else:
					flag = 0
					break
			elif NODES[to] == -1:
				Q.append(to)
	if flag == 0:
		LANS.append('NO')
		continue
	LANS.append('YES')
	for (x, y, c) in EDGE:
		if c != -1:
			LANS.append(str(x) + ' ' + str(y) + ' ' + str(c))
		elif (NODES[x] ^ NODES[y]) % 2 == 0:
			LANS.append(str(x) + ' ' + str(y) + ' 0')
		else:
			LANS.append(str(x) + ' ' + str(y) + ' 1')
sys.stdout.write('\n'.join(LANS))
