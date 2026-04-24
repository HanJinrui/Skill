from itertools import combinations
import random

def dc(a, b):
	c = a ^ b
	c = int(2 ** (c.bit_length() - 1))
	return c

def cal2(a):
	a.sort()
	mp = int(2 ** (a[-1].bit_length() - 1))
	while len(a) > 1:
		p = 0
		if a[0] == mp and len(a) > 2:
			p = 1
		c = a[p] ^ a[-1]
		c = int(2 ** (c.bit_length() - 1))
		del a[-1]
		a[p] = c
		a.sort()
	return a[0]

def cal(a):
	la = len(a)
	a.sort()
	mp = int(2 ** (a[-1].bit_length() - 1))
	mc = 0
	for x in a:
		if x >= mp:
			mc += 1
	if la == 2:
		return dc(a[0], a[1])
	if la == 3:
		if mc == 1:
			return mp
		return min(dc(dc(a[0], a[1]), a[2]), dc(dc(a[2], a[1]), a[0]), dc(dc(a[0], a[2]), a[1]))
	if la == 4:
		if mc == 1:
			return mp
		if mc == 2:
			return 0
		if mc == 3:
			return mp
		if mc == 4:
			return min(dc(dc(dc(a[0], a[1]), a[2]), a[3]), dc(dc(dc(a[2], a[1]), a[0]), a[3]), dc(dc(dc(a[0], a[2]), a[1]), a[3]), dc(dc(a[0], a[1]), dc(a[2], a[3])), dc(dc(a[0], a[2]), dc(a[1], a[3])), dc(dc(a[0], a[3]), dc(a[2], a[1])), dc(dc(dc(a[3], a[1]), a[2]), a[0]), dc(dc(dc(a[3], a[1]), a[0]), a[2]), dc(dc(dc(a[3], a[2]), a[0]), a[1]))
	if la == 5:
		if mc == 1:
			return mp
		if mc == 2:
			return 0
		if mc == 3:
			return mp
		if mc == 4:
			return 0
		if mc == 5:
			return mp
n = int(input())
a = list(map(int, input().split()))
if True:
	result = 0
	res1 = result
	result = 0
	ph = {}
	ap = [0 for _ in range(n)]
	for i in range(n):
		ap[i] = int(2 ** (a[i].bit_length() - 1))
	for i in range(n):
		result += a[i]
	for i in range(n):
		for j in range(max(i - 4, 0), i):
			v1 = cal(ap[j:i + 1])
			v2 = cal(a[j:i + 1])
			if v1 != v2:
				result += abs(v1 - v2)
	for i in range(n):
		p = ap[i]
		phn = {}
		s = 0
		for (k, v) in ph.items():
			(lp, le) = k
			if p < lp:
				phn[k] = v
			if p > lp:
				s += v
		if (p, 0) in ph:
			phn[p, 1] = ph[p, 0] + 1 + s
		else:
			phn[p, 1] = 1 + s
		if (p, 1) in ph:
			phn[p, 0] = ph[p, 1]
		ph = phn
		tr = 0
		for (k, v) in ph.items():
			(lp, le) = k
			if le == 1:
				if lp == p:
					tr += lp * (v - 1)
				else:
					tr += lp * v
		result += tr
		result = result % 998244353
	print(result)
