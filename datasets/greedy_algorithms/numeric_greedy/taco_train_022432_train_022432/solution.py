import sys
from array import array

def input():
	return sys.stdin.buffer.readline().decode('utf-8')
(n, m, b, a, c) = map(int, input().split())

def ng():
	print('IMPOSSIBLE')
	exit()
if n * m & 1:
	ng()
ans = [['*'] * m for _ in range(n)]
if n % 2:
	s = ['y', 'z']
	for (i, j) in enumerate(range(0, m, 2)):
		ans[-1][j] = ans[-1][j + 1] = s[i & 1]
		b -= 1
if m % 2:
	s = ['y', 'z']
	for (i, j) in enumerate(range(0, n, 2)):
		ans[j][-1] = ans[j + 1][-1] = s[i & 1]
		a -= 1
s1 = [['a', 'b'], ['c', 'd']]
s2 = [['e', 'f'], ['g', 'h']]
for i in range(0, n - (n & 1), 2):
	for j in range(0, m - (m & 1), 2):
		if c:
			ans[i][j] = ans[i + 1][j] = ans[i][j + 1] = ans[i + 1][j + 1] = s1[0][0]
			c -= 1
		elif a >= 2:
			ans[i][j] = ans[i + 1][j] = s1[0][0]
			ans[i][j + 1] = ans[i + 1][j + 1] = s1[0][1]
			a -= 2
		else:
			ans[i][j] = ans[i][j + 1] = s1[0][0]
			ans[i + 1][j] = ans[i + 1][j + 1] = s1[0][1]
			b -= 2
		(s1[0], s1[1]) = (s1[1], s1[0])
	(s1, s2) = (s2, s1)
if a < 0 or b < 0:
	ng()
else:
	for row in ans:
		print(*row, sep='')
