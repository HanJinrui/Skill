t = int(input())
for i in range(t):
	(n, e, h, a, b, c) = map(int, input().split())
	l2 = []
	ans = 1e+18
	for j in range(n + 1):
		if j > e or j > h:
			break
		m1 = (e - j) // 2
		m2 = (h - j) // 3
		if n > j + m1 + m2:
			continue
		if a < b:
			r1 = min(n - j, m1)
			r2 = n - j - r1
		else:
			r2 = min(n - j, m2)
			r1 = n - j - r2
		p = j * c + r1 * a + r2 * b
		ans = min(ans, p)
	if ans == 1e+18:
		print(-1)
	else:
		print(ans)
