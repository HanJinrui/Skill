for _ in range(int(input())):
	(n, k) = map(int, input().split())
	a = [*map(int, input().split())]
	q = [0] * 32
	for i in a:
		p = 0
		while i:
			q[p] += i & 1
			i >>= 1
			p += 1
	print(sum(((i + k - 1) // k for i in q)))
