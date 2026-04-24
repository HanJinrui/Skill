for _ in range(int(input())):
	n = int(input())
	ans = 0
	(c1, c2) = ([0] * (n + 1), [0] * (n + 1))
	pairs = []
	for i in range(n):
		(a, b) = map(int, input().split())
		c1[a] += 1
		c2[b] += 1
		pairs += [(a, b)]
	print(n * (n - 1) * (n - 2) // 6 - sum(((c1[a] - 1) * (c2[b] - 1) for (a, b) in pairs)))
