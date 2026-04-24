for _ in range(int(input())):
	(n, k) = map(int, input().split())
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]
	if len(set(a)) < k:
		print(-1)
	else:
		d = {}
		for i in range(n):
			d[a[i]] = min(d.get(a[i], 10 ** 5), b[i])
		v = list(d.values())
		v.sort()
		print(sum(v[:k]))
