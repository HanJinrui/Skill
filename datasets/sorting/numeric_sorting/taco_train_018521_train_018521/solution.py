def fun(a, n, s):
	for i in range(n):
		s += a[i] * (i - (n - i - 1))
	return s * 2
for _ in range(int(input())):
	(n, a, b) = (int(input()), sorted(list(map(int, input().split()))), [])
	for i in range(n - 1):
		for j in range(i + 1, n):
			b.append(a[i] + a[j])
	b.sort()
	print(fun(b, len(b), 0) - fun(a, n, 0) * (n - 2))
