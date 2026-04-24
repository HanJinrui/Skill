R = lambda : [*map(int, input().split())]
(n, m, k) = R()
(p, s, c) = (R(), R(), R())
a = [0] * m
for (x, y) in zip(p, s):
	a[y - 1] = max(a[y - 1], x)
print(sum((p[x - 1] < a[s[x - 1] - 1] for x in c)))
