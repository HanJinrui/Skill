I = input
for _ in [0] * int(I()):
	(a, b, n, m) = map(int, (I() + ' ' + I()).split())
	k = m + 1
	print(n // k * min(a * m, b * k) + n % k * min(a, b))
