import sys
from collections import Counter
N = int(input())
Edge = [[] for _ in range(N)]
Dim = [0] * N
for _ in range(N - 1):
	(a, b) = map(int, sys.stdin.readline().split())
	a -= 1
	b -= 1
	Edge[a].append(b)
	Edge[b].append(a)
	Dim[a] += 1
	Dim[b] += 1

def dfs(x):
	dist = [0] * N
	stack = [x]
	visited = set([x])
	for _ in range(N):
		vn = stack.pop()
		for vf in Edge[vn]:
			if vf not in visited:
				visited.add(vf)
				dist[vf] = 1 + dist[vn]
				stack.append(vf)
	return dist

def check(i):
	dist = dfs(i)
	D = [-1] * N
	for i in range(N):
		if D[dist[i]] == -1:
			D[dist[i]] = Dim[i]
		elif D[dist[i]] != Dim[i]:
			return False
	return True

def getpar(Edge, p):
	N = len(Edge)
	par = [0] * N
	par[p] - 1
	stack = [p]
	visited = set([p])
	while stack:
		vn = stack.pop()
		for vf in Edge[vn]:
			if vf in visited:
				continue
			visited.add(vf)
			par[vf] = vn
			stack.append(vf)
	return par

def solve():
	Leaf = [i for i in range(N) if Dim[i] == 1]
	dist0 = dfs(0)
	md0 = max(dist0)
	p1 = dist0.index(md0)
	distp1 = dfs(p1)
	mdp1 = max(distp1)
	p2 = distp1.index(mdp1)
	if check(p1):
		return p1 + 1
	if check(p2):
		return p2 + 1
	if mdp1 % 2 == 1:
		return -1
	distp2 = dfs(p2)
	for i in range(N):
		if distp1[i] == distp2[i] == mdp1 // 2:
			break
	cen = i
	distcen = dfs(cen)
	if check(cen):
		return cen + 1
	G = [distcen[l] for l in Leaf]
	GC = Counter(G)
	if len(GC) == 1:
		P = getpar(Edge, cen)
		for l in Leaf:
			k = P[l]
			while k != cen:
				if Dim[k] != 2:
					break
				k = P[k]
			else:
				if check(l):
					return l + 1
				else:
					return -1
		return -1
	else:
		sl = set(Leaf)
		for (k, v) in GC.items():
			if v == 1:
				for (i, d) in enumerate(distcen):
					if i in sl and d == k:
						if check(i):
							return i + 1
		return -1
print(solve())
