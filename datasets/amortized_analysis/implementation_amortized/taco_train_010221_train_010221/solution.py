for _ in range(int(input())):
	(n, k) = map(int, input().split())
	s = input().strip()
	c = s[:k].count('W')
	m = c
	for i in range(k, n):
		c += (s[i] == 'W') - (s[i - k] == 'W')
		m = min(m, c)
	print(m)
