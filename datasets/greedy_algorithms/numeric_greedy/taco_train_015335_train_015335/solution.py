for i in range(int(input())):
	(n, m, d) = map(int, input().split())
	p = list(map(int, input().split()))
	a = list(map(int, input().split()))
	ans = n + 1
	v = {}
	for k in range(n):
		v[p[k]] = k
	for j in range(m - 1):
		if v[a[j]] < v[a[j + 1]] <= v[a[j]] + d:
			ans = min(ans, v[a[j + 1]] - v[a[j]])
			if d < n - 1:
				ans = min(ans, v[a[j]] - v[a[j + 1]] + d + 1)
		else:
			ans = 0
	print(ans)
