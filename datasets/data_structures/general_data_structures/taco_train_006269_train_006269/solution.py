(n, m, c) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
(s, k) = (0, n - m)
for i in range(n):
	if i < m:
		s += b[i]
	a[i] = (a[i] + s) % c
	if i >= k:
		s -= b[i - k]
print(' '.join((str(i) for i in a)))
