import math
t = int(input())
for i in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	s = sum(a)
	c = 0
	if s % n == 0:
		a = sorted(a)
		while a[0] != a[n - 1]:
			x = math.ceil((a[n - 1] - a[0]) / 2)
			a[n - 1] -= x
			a[0] += x
			c += 1
			a = sorted(a)
		print(c)
	else:
		print(-1)
