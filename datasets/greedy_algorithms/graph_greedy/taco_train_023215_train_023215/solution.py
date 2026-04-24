import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
x = [0] * (n + 1)
c = 0
for i in range(m):
	(u, v) = map(int, input().split())
	mn = min(u, v)
	if x[mn] == 0:
		c += 1
	x[mn] += 1
q = int(input())
for i in range(q):
	(a, *b) = map(int, input().split())
	if a == 3:
		print(n - c)
	elif a == 1:
		d = min(b)
		if x[d] == 0:
			c += 1
		x[d] += 1
	else:
		d = min(b)
		x[d] -= 1
		if x[d] == 0:
			c -= 1
