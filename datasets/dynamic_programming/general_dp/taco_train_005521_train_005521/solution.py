import sys
n = 6
maxn = 10
reqs = [(0, 1), (1, 2)]
reqs3 = [(1, 3), (1, 2)]
reqs2 = [(1, 3), (0, 1), (2, 4), (0, 4), (2, 5), (3, 4), (0, 2)]

def match_reqs(acc_list, reqs):
	for (a, b) in reqs:
		if acc_list[a] > acc_list[b]:
			return False
	return True

def req(n, reqs, acc_list):
	print(n, reqs, acc_list)
	summ = 0
	if n == 0:
		if match_reqs(acc_list, reqs):
			return 1
		else:
			return 0
	for i in range(maxn):
		summ += req(n - 1, reqs, acc_list + [i])
	return summ

def req2(n, reqs):
	if n == 0:
		assert reqs == []
		return list(map(lambda x: [x], range(maxn)))
	(reqs1, reqs2) = split_reqs(reqs, n)
	solutions = []
	subsolutions = req2(n - 1, reqs1)
	print(n, len(subsolutions))
	print('FUCK YOU')
	for i in range(maxn):
		solutions += filter_list(subsolutions, i, reqs2)
	return solutions

def req22(n, reqs):
	return len(req2(n - 1, reqs)) % 1007

def split_reqs(reqs, n):
	reqs1 = []
	reqs2 = []
	for (a, b) in reqs:
		if a == n or b == n:
			reqs2.append((a, b))
		else:
			reqs1.append((a, b))
	return (reqs1, reqs2)

def filter_list(solutions, newval, reqs):
	result = []
	for solution in solutions:
		if match_reqs(solution + [newval], reqs):
			result.append(solution + [newval])
	return result
from operator import mul
from functools import reduce

def rlen(r):
	(a, b) = r
	if a > b:
		return 0
	return b - a + 1

def update_ranges(ranges, val, reqs):
	removed_var = len(ranges)
	updated = list(ranges)
	for (a, b) in reqs:
		if a == removed_var:
			(x, y) = updated[b]
			if val > x:
				updated[b] = (val, y)
		if b == removed_var:
			(x, y) = updated[a]
			if val < y:
				updated[a] = (x, val)
	return updated
memodict = {}

def req3(ranges, reqs):
	if reqs == []:
		return reduce(mul, map(rlen, ranges), 1)
	key = (tuple(ranges), tuple(reqs))
	if key in memodict:
		return memodict[key]
	summ = 0
	lastr = ranges[-1]
	rest = ranges[:-1]
	(a, b) = lastr
	(unrelated, related) = split_reqs(reqs, len(rest))
	for val in range(a, b + 1):
		updated = update_ranges(rest, val, related)
		summ += req3(updated, unrelated)
	summ = summ % 1007
	memodict[key] = summ
	return summ

def req33(n, reqs):
	return req3([(0, maxn - 1)] * n, reqs) % 1007

def runcommand():
	req_list = []
	(n, m) = map(int, sys.stdin.readline().split())
	for _ in range(m):
		(a, b) = map(int, sys.stdin.readline().split())
		req_list.append((a, b))
	print(req33(n, req_list))
runcommand()
