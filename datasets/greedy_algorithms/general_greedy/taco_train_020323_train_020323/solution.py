for i in range(int(input())):
	(n, k) = map(int, input().split())
	l = input()
	d = {}
	for i in l:
		if i in d:
			d[i] += 1
			continue
		d[i] = 1
	if max(d.values()) - min(d.values()) > k:
		print(-1)
		continue
	a = ''
	x = sorted(d.keys())
	for i in range(n):
		for j in x:
			if d[j] == 0:
				continue
			d[j] -= 1
			if max(d.values()) - min(d.values()) <= k:
				a += j
				break
			d[j] += 1
	print(a)
