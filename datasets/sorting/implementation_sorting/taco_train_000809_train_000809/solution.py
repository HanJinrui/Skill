R = lambda : map(int, input().split())
(n, m) = R()
a = [[], []]
for (x, y) in zip(R(), R()):
	a[y] += [x]
d = [(x + y) // 2 for (x, y) in zip(a[1], a[1][1:])] + [1 << 30]
s = [0] * m
i = 0
for x in a[0]:
	while x > d[i]:
		i += 1
	s[i] += 1
print(*s)
