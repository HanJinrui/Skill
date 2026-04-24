import sys
sys.setrecursionlimit(110000)
mod = 10 ** 9 + 7

def solve(t, i, parent):
	arr = []
	for child in t[i]:
		if child != parent:
			arr.append(solve(t, child, i))
	arr.sort(reverse=True)
	_sum = 1
	for (i, j) in enumerate(arr):
		_sum += (i + 1) * j
	return _sum
for _ in range(int(input())):
	(n, x) = list(map(int, input().split(' ')))
	t = [[] for i in range(n + 1)]
	for i in range(n - 1):
		(u, v) = list(map(int, input().split(' ')))
		t[u].append(v)
		t[v].append(u)
	print(x * solve(t, 1, 0) % mod)
