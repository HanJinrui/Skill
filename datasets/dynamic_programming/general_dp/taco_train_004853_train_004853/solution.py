q = int(input())
for Q in range(q):
	n = int(input())
	a = [int(x) for x in input().split()]
	s = 0
	for x in a:
		if x == 1:
			s += 1
	out = [s]
	m = n * n
	for k in range(2, n + 1):
		r = n - k + 1
		s = 0
		for i in range(r + 1):
			for j in range(r + 1):
				b = n * j + m * i
				for h in range(b, b + r):
					if a[h + 1] > a[h]:
						a[h] = a[h + 1]
		for i in range(r + 1):
			for j in range(r):
				b = n * j + m * i
				for h in range(b, b + r):
					if a[h + n] > a[h]:
						a[h] = a[h + n]
		for i in range(r):
			for j in range(r):
				b = n * j + m * i
				for h in range(b, b + r):
					if a[h + m] > a[h]:
						a[h] = a[h + m]
					if a[h] == k:
						s += 1
		out.append(s)
	print(*out)
