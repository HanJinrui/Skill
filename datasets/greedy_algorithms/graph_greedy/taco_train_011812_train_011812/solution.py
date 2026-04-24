for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	(d, c) = ([0] * n, 0)
	for i in range(1, n):
		if l[i - 1] > l[i]:
			c += 1
		d[i] = d[c] + 1
	print(d[n - 1])
