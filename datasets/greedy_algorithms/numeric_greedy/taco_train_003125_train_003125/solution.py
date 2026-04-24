from math import gcd
for i in range(int(input())):
	(n, k) = map(int, input().split())
	a = list(map(int, input().split()))
	g = 0
	for i in a:
		g = gcd(g, i)
	g1 = 0
	c = 0
	for i in a:
		g1 = gcd(g1, i)
		if g1 == g:
			c += 1
			g1 = 0
	if c >= k:
		print('YES')
	else:
		print('NO')
