from collections import defaultdict as dd, deque
import sys
input = sys.stdin.readline

def cycle_part(C, n):
	P = [-1] * n
	root = 0
	Q = [(root, root)]
	O = [None] * n
	depth = 0
	cycs = []
	while Q:
		(u, par) = Q.pop()
		if P[u] != -1:
			if O[u] < O[par] and P[par] != u:
				cycs.append((par, u))
			continue
		P[u] = par
		O[u] = depth
		depth += 1
		for v in C[u]:
			if v != par:
				Q.append((v, u))
	which_cyc = dd(lambda : -1)
	cycles = []
	for (fro, to) in cycs:
		v = fro
		ix = len(cycles)
		cycle = [fro]
		which_cyc[fro] = ix
		while v != to:
			v = P[v]
			which_cyc[v] = ix
			cycle.append(v)
		cycles.append(cycle)
	return (cycles, which_cyc, P, O)
t = int(input())
for _ in range(t):
	(n, m) = map(int, input().split())
	C = [[] for _ in range(n)]
	E = []
	for _ in range(m):
		(a, b) = map(int, input().split())
		a -= 1
		b -= 1
		C[a].append(b)
		C[b].append(a)
		E.append((a, b))
	(cycles, which_cyc, P, O) = cycle_part(C, n)
	C_cyc = [[] for _ in range(n)]
	E_cyc = []
	for cycle in cycles:
		for i in range(len(cycle)):
			j = (i + 1) % len(cycle)
			a = cycle[i]
			b = cycle[j]
			C_cyc[a].append(b)
			C_cyc[b].append(a)
			C[a].remove(b)
			C[b].remove(a)
	V = {i for i in range(n) if C[i]}
	Pt = [-1] * n
	Ot = []
	for root in V:
		Q = [(root, root)]
		while Q:
			(v, par) = Q.pop()
			if Pt[v] != -1:
				continue
			Pt[v] = par
			Ot.append(v)
			for u in C[v]:
				Q.append((u, v))
	ways_down = [0] * n
	for v in reversed(Ot):
		if Pt[v] != v:
			ways_down[Pt[v]] += ways_down[v] + 1
	ways_up = [0] * n
	for v in Ot:
		ways_up[v] = ways_up[Pt[v]] + ways_down[Pt[v]] - 1 - ways_down[v] + 1
	ways_down2 = [0] * n
	for cycle in cycles:
		for i in range(len(cycle)):
			a = cycle[i]
			b = cycle[i - 1]
			ways_down2[a] += ways_down[b] + ways_up[b] + 1
			ways_down2[b] += ways_down[a] + ways_up[a] + 1
	for v in reversed(Ot):
		if Pt[v] != v:
			ways_down2[Pt[v]] += ways_down2[v] + 1
	ways_up2 = [0] * n
	for v in Ot:
		ways_up2[v] = ways_up2[Pt[v]] + ways_down2[Pt[v]] - 1 - ways_down2[v] + 1
	res = [-1] * m
	for i in range(m):
		(a, b) = E[i]
		if which_cyc[a] == which_cyc[b] != -1:
			prod = 1
			if a in V:
				prod *= ways_down[a] + ways_up[a] + 1
			if b in V:
				prod *= ways_down[b] + ways_up[b] + 1
			res[i] = prod
		else:
			if Pt[a] == b:
				parent = b
				child = a
			else:
				parent = a
				child = b
			res[i] = (1 + ways_down2[child]) * ways_up[child] + (1 + ways_down[child]) * ways_up2[child] - (1 + ways_down[child]) * ways_up[child]
	print(*res, sep='\n')
