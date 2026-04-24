for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = []
	s = 0
	for i in range(n):
		s += a[i]
		b.append(s)
	if s == 0:
		c = 0
		for i in range(n):
			if b[i] != 0:
				c += 1
		print(c)
	else:
		for i in range(n, 0, -1):
			if s % i == 0:
				d = s // i
				e = d
				for j in range(n):
					if b[j] == e:
						e += d
					if e - d == s:
						break
				if e - d == s:
					print(n - i)
					break
