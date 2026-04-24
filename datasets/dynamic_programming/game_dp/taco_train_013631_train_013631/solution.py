(a, b, L) = list(map(int, input().split()))
import sys
import math
if a == 1 and 2 ** b >= L:
	print('Missing')
	sys.exit()
memo = {}
memo[32001, 1] = 0
memo[1, 30] = 0
for i in range(min(int(L ** (1 / b)) + 1, 32000), a - 1, -1):
	for j in range(29, b - 1, -1):
		if i ** j >= L:
			continue
		s = set()
		if (i + 1) ** j < L:
			s.add(memo[i + 1, j])
		if i ** (j + 1) < L:
			s.add(memo[i, j + 1])
		mex = 0
		while mex in s:
			mex += 1
		memo[i, j] = mex
if memo[a, b] > 0:
	print('Masha')
else:
	print('Stas')
