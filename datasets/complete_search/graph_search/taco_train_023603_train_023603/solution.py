import sys
import io, os
input = sys.stdin.buffer.readline
(n, m, k) = map(int, input().split())
AB = []
g = [[] for _ in range(n)]
for i in range(m):
	(a, b) = map(int, input().split())
	(a, b) = (a - 1, b - 1)
	g[a].append(b)
	g[b].append(a)
	AB.append((a, b))
from collections import deque
q = deque([])
q.append(0)
d = [-1] * n
d[0] = 0
while q:
	v = q.popleft()
	for u in g[v]:
		if d[u] == -1:
			d[u] = d[v] + 1
			q.append(u)
inc = [[] for _ in range(n)]
for (i, (a, b)) in enumerate(AB):
	if d[a] + 1 == d[b]:
		inc[b].append(i)
	if d[b] + 1 == d[a]:
		inc[a].append(i)
F = [0] * n
res = []
for i in range(k):
	s = ['0'] * m
	for j in range(1, n):
		s[inc[j][F[j]]] = '1'
	res.append(''.join(s))
	flag = False
	for j in range(1, n):
		if F[j] + 1 < len(inc[j]):
			flag = True
			F[j] += 1
			break
		else:
			F[j] = 0
	if not flag:
		break
print(len(res))
print(*res, sep='\n')
