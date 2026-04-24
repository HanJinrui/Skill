import sys
from sys import stdin
import math
from collections import deque
n = int(stdin.readline())
dic = {}
lis = []
for i in range(n):
	(a, b, c, d) = map(int, stdin.readline().split())
	(A, B, C, D) = (a + b, b, c, d)
	siA = C * B
	boA = D * A
	g = math.gcd(siA, boA)
	siA //= g
	boA //= g
	if (siA, boA) not in dic:
		dic[siA, boA] = len(dic)
		lis.append([])
	(A, B, C, D) = (a, b, c + d, d)
	siB = C * B
	boB = D * A
	g = math.gcd(siB, boB)
	siB //= g
	boB //= g
	if (siB, boB) not in dic:
		dic[siB, boB] = len(dic)
		lis.append([])
	va = dic[siA, boA]
	vb = dic[siB, boB]
	lis[va].append((vb, i))
	lis[vb].append((va, i))
ans = []
used = [False] * (3 * n)
nexedge = [0] * (3 * n)
able = [True] * (3 * n)
pedge = [None] * (3 * n)
for v in range(len(lis)):
	if not able[v]:
		continue
	stk = [v]
	able[v] = False
	while stk:
		v = stk[-1]
		if len(lis[v]) <= nexedge[v]:
			elis = []
			for (nex, ind) in lis[v]:
				if ind != pedge[v] and (not used[ind]):
					elis.append(ind)
			if pedge[v] != None and (not used[pedge[v]]):
				elis.append(pedge[v])
			for i in range(1, len(elis), 2):
				ans.append((elis[i - 1] + 1, elis[i] + 1))
				used[elis[i - 1]] = True
				used[elis[i]] = True
			del stk[-1]
			continue
		(nex, ind) = lis[v][nexedge[v]]
		nexedge[v] += 1
		if able[nex]:
			pedge[nex] = ind
			able[nex] = False
			stk.append(nex)
print(len(ans))
for i in ans:
	print(*i)
