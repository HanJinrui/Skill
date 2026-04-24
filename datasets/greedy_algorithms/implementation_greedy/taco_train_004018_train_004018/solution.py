import sys
from math import sqrt, gcd, factorial, ceil, floor, pi
from collections import deque, Counter, OrderedDict
from heapq import heapify, heappush, heappop
input = lambda : sys.stdin.readline()
I = lambda : int(input())
S = lambda : input().strip()
M = lambda : map(int, input().strip().split())
L = lambda : list(map(int, input().strip().split()))
mod = 1000000007
for _ in range(I()):
	n = I()
	p = L()
	s = L()
	ans = 'YES' if p[-1] == s[0] else 'NO'
	for i in range(n):
		if i == 0 and p[i] != 1 or (i > 0 and p[i] not in [p[i - 1], p[i - 1] + 1]):
			ans = 'NO'
			break
	for i in range(n)[::-1]:
		if i == n - 1 and s[i] != 1 or (i < n - 1 and s[i] not in [s[i + 1], s[i + 1] + 1]):
			ans = 'NO'
			break
	if ans == 'NO':
		print(ans)
		continue
	st = []
	for i in range(n):
		(a, b) = (p[i] - (p[i - 1] if i - 1 >= 0 else 0), s[i] - (s[i + 1] if i + 1 < n else 0))
		if a and (not b):
			st.append('(')
		elif b and (not a):
			if st:
				st.pop()
			else:
				ans = 'NO'
				break
		elif not b and (not a):
			if not st:
				ans = 'NO'
				break
	print(ans)
