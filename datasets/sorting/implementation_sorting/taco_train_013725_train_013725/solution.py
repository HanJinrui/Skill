I = lambda : list(map(int, input().split()))
(n, k) = I()
a = I()
b = I()
l = 0
r = 2 * 10 ** 9
while l < r:
	m = (l + r) // 2 + 1
	s = sum((max(a[i] * m - b[i], 0) for i in range(n)))
	if s > k:
		r = m - 1
	else:
		l = m
print(l)
