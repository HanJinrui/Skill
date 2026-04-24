R = lambda : map(int, input().split())
(n, k, l) = R()
a = sorted(R())
s = c = 0
for i in range(n * k - 1, -1, -1):
	c += 1
	if a[i] - a[0] <= l and c >= k:
		s += a[i]
		c -= k
print((s, 0)[c > 0])
