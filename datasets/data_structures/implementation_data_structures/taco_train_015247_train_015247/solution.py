for i in range(int(input())):
	(n, m, k) = map(int, input().split())
	l = list(map(int, input().split()))
	d = set()
	r = set()
	for j in l:
		if j <= n:
			if j in d:
				r.add(j)
			else:
				d.add(j)
	r = list(r)
	r.sort()
	print(len(r), *r)
