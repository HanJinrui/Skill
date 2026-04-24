R = lambda : map(int, input().split())
(n, m, k) = R()
a = [*R()]
(i, s) = (n, k)
while i and m:
	i -= 1
	if s < a[i]:
		m -= 1
		s = k
	s -= a[i]
print(n - i - (m == 0))
