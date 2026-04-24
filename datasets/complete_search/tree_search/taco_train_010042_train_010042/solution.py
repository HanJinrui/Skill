for _ in range(int(input())):
	(n, m) = map(int, input().split())
	r = [1] * n
	for i in range(m):
		(x, y, z) = map(int, input().split())
		r[y - 1] = 0
	q = r.index(1) + 1
	for i in range(1, n + 1):
		if i != q:
			print(q, i)
