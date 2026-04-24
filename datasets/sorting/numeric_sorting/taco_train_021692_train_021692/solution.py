(a, b, c) = map(int, input().split())
(l, h) = (0, a)
r = 1
z = 0
(p, q) = (b - 1, a - b)
while l < h:
	m = (l + h) // 2
	if m == c:
		z += 1
		l = m + 1
	elif m > c:
		z += 1
		r *= q
		q -= 1
		h = m
	else:
		z += 1
		r *= p
		p -= 1
		l = m + 1
for i in range(2, a - z + 1):
	r = r * i % 1000000007
print(r)
