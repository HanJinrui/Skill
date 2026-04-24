import sys
from collections import deque
oo = float('inf')

def augment(res, u, t, level, limit):
	if limit == 0:
		return 0
	if u == t:
		return limit
	flow = 0
	for v in range(len(res)):
		if res[u][v] > 0 and level[v] == level[u] + 1:
			aug = augment(res, v, t, level, min(limit, res[u][v]))
			res[u][v] -= aug
			res[v][u] += aug
			flow += aug
			limit -= aug
	if not flow:
		level[u] = None
	return flow

def dinic(res):
	q = deque()
	max_flow = 0
	while True:
		q.append(s)
		level = [None] * len(res)
		level[s] = 0
		while q:
			u = q.popleft()
			for v in range(len(res)):
				if res[u][v] > 0 and level[v] == None:
					level[v] = level[u] + 1
					q.append(v)
		if level[t] == None:
			return max_flow
		max_flow += augment(res, s, t, level, sum((res[s][v] for v in range(len(res)))))
T = int(sys.stdin.readline())
for _ in range(T):
	(N, M) = map(int, sys.stdin.readline().split())
	(s, t) = (0, 2 * N + 1)
	res = [[0] * (t + 1) for _ in range(t + 1)]
	for i in range(N):
		(res[s][i + 1], res[i + 1 + N][t]) = (1, 1)
	for i in range(M):
		(A, B) = map(int, sys.stdin.readline().split())
		if A != B:
			res[A][B + N] = 1
	max_flow = dinic(res)
	print(N - max_flow)
