R = lambda : map(int, input().split())
(n, k) = R()
a = [list(R()) for _ in range(n)]
p = [0.0] * k
d = 0
for r in a:
	s = sum(r) + d
	d = 1
	p = [(x + y) / s for (x, y) in zip(r, p)]
print(*p)
