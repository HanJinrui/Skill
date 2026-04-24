for i in range(int(input())):
	(n, m) = map(int, input().split())
	l = [0] * m
	ans = 0
	for i in range(n):
		c = list(input())
		l = [int(i) + int(j) for (i, j) in zip(l, c)]
	for j in l:
		ans += j * (j - 1) // 2
	print(ans)
