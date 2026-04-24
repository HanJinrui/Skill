R = lambda : map(int, input().split())
(n, m) = R()
e = 0
for _ in range(n):
	(a, b) = R()
	if a <= e:
		e = max(e, b)
print('NO' if e < m else 'YES')
