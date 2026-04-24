f = lambda : map(int, input().split())
(n, a, b) = f()
(p, s) = (0, a + b)
t = [((x, y), x * y, x + y) for (x, y) in [f() for i in range(n)]]
for (k, (qo, po, so)) in enumerate(t, 1):
	for (qk, pk, sk) in t[k:]:
		if any((i + j <= d <= s - max(so - i, sk - j) for i in qo for j in qk for d in [a, b])):
			p = max(p, po + pk)
print(p)
