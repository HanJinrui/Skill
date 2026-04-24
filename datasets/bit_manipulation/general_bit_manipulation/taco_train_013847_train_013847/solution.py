for _ in range(int(input())):
	n = int(input())
	k = 1
	while k << 1 < n:
		k <<= 1
	print(*range(k - 1, -1, -1), *range(k, n))
