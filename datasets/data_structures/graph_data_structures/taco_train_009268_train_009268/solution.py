import math
for _ in range(int(input())):
	(n, m) = map(int, input().split())
	if m < n - 1 or m > n * (n + 1) / 2:
		print(-1)
	elif n == 1 and m == 0:
		print(0)
	elif m == 1:
		print(1)
	elif m <= n + 1:
		print(2)
	else:
		l = m - 2 * n
		if l > 0:
			print(math.ceil(l * 2 / n) + 3)
		else:
			print(3)
