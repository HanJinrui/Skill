tc = int(input())
while tc > 0:
	(n, m) = map(int, input().split())
	k = n + m - 1
	c = [[0, 0] for _ in range(k)]
	for i in range(n):
		for (j, v) in enumerate(input().split()):
			c[i + j][int(v)] += 1
	ans = 0
	for i in range(k // 2):
		ans += min(c[i][0] + c[k - i - 1][0], c[i][1] + c[k - i - 1][1])
	print(ans)
	tc -= 1
