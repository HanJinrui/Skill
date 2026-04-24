for _ in range(int(input())):
	n = int(input())
	s = input()
	s = s + ' '
	m = []
	c = 1
	M = 0
	for i in range(n):
		if s[i] != s[i + 1]:
			if c >= M:
				M = c
				m.append(s[i])
			c = 1
		else:
			c += 1
	for j in m:
		if s.count(M * j) > 1:
			print(M)
			break
	else:
		print(M - 1)
