import math
(n, m) = map(int, input().split())
m = min(n, m)
if n == m:
	print(n)
else:
	n -= m
	n += n
	x = math.ceil(n ** 0.5)
	while (x - 1) * x >= n:
		x -= 1
	print(x + m)
