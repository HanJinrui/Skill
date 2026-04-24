i = lambda : map(int, input().split())
(n, m) = i()
r = []
for _ in range(n):
	(a, b) = i()
	m -= b
	r += [a - b]
for iv in sorted(r):
	if m >= iv:
		m -= iv
		n -= 1
print(-1 if m < 0 else n)
