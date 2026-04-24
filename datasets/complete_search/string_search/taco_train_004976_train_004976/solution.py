for i in range(int(input())):
	n = int(input())
	s = input()
	a = 0
	for i in range(n):
		p = 0
		m = 0
		for j in range(i, n):
			if s[j] == '+':
				p += 1
			else:
				m += 1
			a += (m - p) % 3 == 0 and m >= p
	print(a)
