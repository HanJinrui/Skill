(n, a, b, i) = (int(input()) + 1, 0, 0, 1)
d = [0] * n
while i < n:
	for j in range(i, n, i):
		d[j] += 1
	a = b % 998244353 + d[i]
	b += a
	i += 1
print(a)
