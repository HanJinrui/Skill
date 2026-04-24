for _ in range(int(input())):
	(n, k) = list(map(int, input().split()))
	a = list(map(int, input().split()))
	c = 0
	d = {}
	l = 0
	r = 0
	sm = 0
	m = 1
	i = 0
	while i < n:
		if a[i] > k:
			if a[i] not in d or d[a[i]] == -1:
				c += 1
			d[a[i]] = i
			if c > 1:
				l = d[sm] + 1
				d[sm] = -1
				c -= 1
			sm = a[i]
		r += 1
		i += 1
		if r - l > m:
			m = r - l
	print(m)
