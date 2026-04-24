f = lambda : map(int, input().split())
(a, b) = f()
(c, d) = f()
g = lambda k: 0 if k % p else 1 + g(k // p)
k = 0
for p in (3, 2):
	s = g(a) + g(b) - g(c) - g(d)
	q = p - 1
	for i in range(abs(s)):
		k += 1
		if s > 0:
			if g(a):
				a = a * q // p
			else:
				b = b * q // p
		elif g(c):
			c = c * q // p
		else:
			d = d * q // p
if a * b != c * d:
	print(-1)
else:
	print(k, a, b, c, d)
