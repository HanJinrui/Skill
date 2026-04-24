t = int(input())
for _ in range(t):
	n = int(input())
	r = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]
	d = {sum(r): 0}
	for i in range(n):
		e = dict(d)
		for j in d:
			(p, q) = (j - r[i], d[j] + b[i])
			if p in e:
				e[p] = max(e[p], q)
			else:
				e[p] = q
		d = dict(e)
	ans = 0
	for i in d:
		ans = max(ans, min(i, d[i]))
	print(ans)
