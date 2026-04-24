t = int(input())
for i in range(t):
	(n, k) = map(int, input().split())
	l = list(map(int, input().split()))
	c = 0
	for j in range(n - 1, -1, -1):
		if j > 0:
			c += (l[j] - l[j - 1] - 1) * ((n - j - 1) // k + 1)
		else:
			c += (l[j] - 1) * ((n - j - 1) // k + 1)
	print(c)
