from math import ceil
for t in range(int(input())):
	(n, k, s) = tuple(map(int, input().split()))
	t = ceil(s * k / n)
	print(-1 if t > s - s // 7 else t)
