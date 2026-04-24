from collections import Counter, defaultdict, deque
import itertools
import re
import math
from functools import reduce
import operator
import bisect
from heapq import *
import functools
mod = 998244353
import sys
input = sys.stdin.readline

def Cartesian_Tree(a):
	n = len(a)
	g = [[] for _ in range(n)]
	p = [-1] * n
	st = []
	for i in range(n):
		prv = -1
		while st and a[i] > a[st[-1]]:
			prv = st.pop()
		if prv != -1:
			p[prv] = i
		if st:
			p[i] = st[-1]
		st.append(i)
	root = -1
	for i in range(n):
		if p[i] != -1:
			g[p[i]].append(i)
		else:
			root = i
	return (g, root)
INF = 1 << 31
t = int(input())
for _ in range(t):
	(n, q) = map(int, input().split())
	a = list(map(int, input().split()))
	sa = sum(a)
	x = list(map(int, input().split()))
	(g, root) = Cartesian_Tree(a)
	xx = sorted(x)
	ans = [0] * (q + 1)
	go = deque([[root, q]])
	while go:
		(now, midx) = go.pop()
		if len(g[now]) == 2:
			dif = a[now] - max(a[g[now][0]], a[g[now][1]])
			idx = bisect.bisect_right(xx, dif)
			if idx > 0:
				ans[0] -= 2 * a[now]
				ans[min(midx, idx)] += 2 * a[now]
			midx = min(midx, idx)
		elif len(g[now]) == 1:
			dif = a[now] - a[g[now][0]]
			idx = bisect.bisect_right(xx, dif)
			if idx > 0:
				ans[0] -= 2 * a[now]
				ans[min(midx, idx)] += 2 * a[now]
			midx = min(midx, idx)
		else:
			ans[0] -= 2 * a[now]
			ans[midx] += 2 * a[now]
		for i in g[now]:
			go.append([i, midx])
	for i in range(1, q):
		ans[i] += ans[i - 1]
	for i in range(q):
		ans[i] += sa
	rans = [0] * q
	for i in range(q):
		idx = bisect.bisect_right(xx, x[i])
		rans[i] = ans[idx - 1]
	print(*rans)
