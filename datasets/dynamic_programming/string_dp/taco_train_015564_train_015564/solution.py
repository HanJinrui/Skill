#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, math, random, operator
from string import ascii_lowercase
from string import ascii_uppercase
from fractions import Fraction, gcd
from decimal import Decimal, getcontext
from itertools import product, permutations, combinations
from queue import Queue, PriorityQueue
from collections import deque, defaultdict, Counter
getcontext().prec = 100

MOD = 10**9 + 7
INF = float("+inf")

if sys.subversion[0] != "CPython":  # PyPy?
	raw_input = lambda: sys.stdin.readline().rstrip()
pr = lambda *args: sys.stdout.write(" ".join(str(x) for x in args) + "\n")
epr = lambda *args: sys.stderr.write(" ".join(str(x) for x in args) + "\n")
die = lambda *args: pr(*args) ^ exit(0)

read_str = raw_input
read_strs = lambda: input().split()
read_int = lambda: int(input())
read_ints = lambda: list(map(int, input().split()))
read_float = lambda: float(input())
read_floats = lambda: list(map(float, input().split()))

"---------------------------------------------------------------"

N, M, K = read_ints()
s = read_str()
t = read_str()

for off in range(1, len(s) + 1):
	a = s[off:]
	if a == s[:len(a)]:
		break
else:
	assert 0

alphanum = {c:ascii_lowercase.index(c) for c in ascii_lowercase}

dist = {
	(a, b): min(abs(ca - cb), abs(ca + 26 - cb), abs(cb + 26 - ca))
	for a, ca in list(alphanum.items())
	for b, cb in list(alphanum.items())
}

suflen = off
suf = s[-off:]

def calc_cost(i, w):
	if i + len(w) > len(t):
		return None
	cost = 0
	for x, y in zip(w, t[i:]):
		cost += dist[x, y]
	return cost

cost_full = [calc_cost(i, s) for i in range(len(t) + 1)]
cost_suf = [calc_cost(i, suf) for i in range(len(t) + 1)]
# pr(dist['c', 'b'])
# pr(dist['b', 'c'])
#pr(cost_full)
#pr(cost_suf)
dp = [{} for i in range(len(t) + 1)]
dp[len(t)][0] = 0
# dp[pos][num_occur] = cost

ans = 0
for i in reversed(list(range(len(t)))):
	dpcur = dp[i] = dp[i+1].copy()
	pos = i + len(s)
	num1 = 1
	cost1 = cost_full[i]
	while pos <= len(t):
		for num2, cost2 in list(dp[pos].items()):
			num = num1 + num2
			cost = cost1 + cost2
			if cost > K:
				continue
			ans = max(ans, num)
			if num not in dpcur:
				dpcur[num] = cost
			else:
				dpcur[num] = min(dpcur[num], cost)
		pos += suflen
		if pos > len(t):
			break
		num1 += 1
		cost1 += cost_suf[pos - suflen]

print(ans)
