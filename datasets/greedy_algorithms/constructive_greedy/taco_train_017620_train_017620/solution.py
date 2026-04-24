(n, m) = map(int, input().split())
r = [0]
b = r * n
a = [int(input().replace(' ', ''), 2) for _ in b]
for i in range(1, n):
	for j in range(1, m):
		k = 3 << m - j - 1
		if a[i - 1] & a[i] & k == k:
			r[0] += 1
			r += (i, j)
			b[i - 1] |= k
			b[i] |= k
print(*(r, [-1])[a != b])
