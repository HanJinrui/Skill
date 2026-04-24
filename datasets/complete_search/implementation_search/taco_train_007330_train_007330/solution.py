for _ in range(int(input())):
	n = int(input())
	c = 0
	a = [int(i) for i in input().split()]
	for i in range(n):
		(m, s) = (1, 0)
		for j in range(i, n):
			m *= a[j]
			s += a[j]
			if m == s:
				c += 1
	print(c)
