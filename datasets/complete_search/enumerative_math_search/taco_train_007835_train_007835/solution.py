p = lambda x: x * (x - 1) // 2
(n, r) = (int(input()), 0)
a = [input() for _ in [0] * n]
for _ in [0, 0]:
	r += sum((p(x.count('C')) for x in a))
	a = zip(*a)
print(r)
