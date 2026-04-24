for i in range(int(input())):
	(n, m, a, b) = map(int, input().split())
	x = m - a
	(s, t) = ('', '1' * a + '0' * x)
	for i in range(n):
		s += '\n' + t
		t = t[x:] + t[:x]
	print('YES' + s if n * a == m * b else 'NO')
