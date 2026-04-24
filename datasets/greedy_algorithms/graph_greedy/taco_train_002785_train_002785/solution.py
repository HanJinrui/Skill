import sys
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def ngsearch(x):
	for to in E[x]:
		if NG[to] == 0:
			NG[to] = 1
			Q.append(to)
t = int(input())
for tests in range(t):
	(n, m) = map(int, input().split())
	E = [[] for i in range(n + 1)]
	for i in range(m):
		(x, y) = map(int, input().split())
		E[x].append(y)
		E[y].append(x)
	OK = [0] * (n + 1)
	NG = [0] * (n + 1)
	Q = []
	ngsearch(1)
	while Q:
		x = Q.pop()
		for to in E[x]:
			if NG[to] == 0:
				OK[to] = 1
				ngsearch(to)
	count = 0
	ANS = []
	for i in range(1, n + 1):
		if OK[i] == 1 or NG[i] == 1:
			count += 1
		if OK[i] == 1:
			ANS.append(i)
	if count == n:
		print('YES')
		print(len(ANS))
		print(*ANS)
	else:
		print('NO')
