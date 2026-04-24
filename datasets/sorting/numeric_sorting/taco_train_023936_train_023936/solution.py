import math
(a, b) = map(int, input().split())
n = int(input())
l = []
d = math.gcd(a, b)
for i in range(1, int(d ** (1 / 2) + 1)):
	if d % i == 0:
		l.append(i)
		if i * i != d:
			l.append(d // i)
for j in range(n):
	m = []
	(x, y) = map(int, input().split())
	r = -1
	for k in l:
		if k >= x and k <= y:
			r = max(r, k)
	print(r)
