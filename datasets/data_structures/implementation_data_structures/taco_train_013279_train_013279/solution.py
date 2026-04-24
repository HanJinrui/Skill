(n, m) = map(int, input().split())
a = [x == '.' for x in input()] + [False]
k = sum([a[i] and a[i + 1] for i in range(n)])
t = [0] * m
for i in range(m):
	(x, c) = input().split()
	(x, c) = (int(x) - 1, c == '.')
	k -= (a[x] - c) * (a[x - 1] + a[x + 1])
	(a[x], t[i]) = (c, k)
print('\n'.join(map(str, t)))
