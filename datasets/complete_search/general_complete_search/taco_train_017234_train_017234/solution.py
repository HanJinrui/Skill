from itertools import chain

def Match_Size(Edges):
	(S, T, M) = (set(), set(), set())
	G = {}
	TrG = {}
	for (dist, start, end) in Edges:
		S.add(start)
		T.add(end)
		if start not in G:
			G[start] = []
		G[start].append(end)
		if end not in G:
			G[end] = []
		if end not in TrG:
			TrG[end] = []
		TrG[end].append(start)
		if start not in TrG:
			TrG[start] = []
	while S:
		s = S.pop()
		(Q, P) = ({s}, {})
		while Q:
			u = Q.pop()
			if u in T:
				T.remove(u)
				break
			forw = (v for v in G[u] if (u, v) not in M)
			back = (v for v in TrG[u] if (v, u) in M)
			for v in chain(forw, back):
				if v in P:
					continue
				P[v] = u
				Q.add(v)
		while u != s:
			(u, v) = (P[u], u)
			if v in G[u]:
				M.add((u, v))
			else:
				M.remove((v, u))
	return len(M)
(N, M, K) = map(int, input().split())
a = []
b = []
for n in range(N):
	(y, x) = map(int, input().split())
	a.append((n, y, x))
for m in range(M):
	(y, x) = map(int, input().split())
	b.append((m, y, x))
c = []
for (n, y1, x1) in a:
	for (m, y2, x2) in b:
		dist = (y2 - y1) ** 2 + (x2 - x1) ** 2
		c.append((dist, n, N + m))
c = sorted(c)
lo = 0
hi = len(c) - 1
while lo < hi:
	mid = (hi + lo) // 2
	match_size = Match_Size(c[:mid + 1])
	if match_size >= K:
		hi = mid
	else:
		lo = mid + 1
print(c[lo][0])
