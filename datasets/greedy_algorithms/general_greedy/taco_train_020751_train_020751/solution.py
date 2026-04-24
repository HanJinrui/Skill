R = lambda : map(int, input().split())
(n, x) = R()
(c, d) = (set(R()), set())
a = (2, 0)[len(c) < n]
for y in c:
	if y != y & x and y & x in c:
		a = min(a, 1)
	d |= {y & x}
print((-1, a)[len(d) < n])
