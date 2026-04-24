((n, k), t) = (map(int, input().split()), sorted(map(int, input().split())))
(i, d, s) = (1, t[0], sum(t))
while i < n and 100 * s - k * (s - d) > t[i] * (100 * n - k * (n - i)):
	d += t[i]
	i += 1
print((100 * s - k * (s - d)) / (100 * n - k * (n - i)))
