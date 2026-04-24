(n, a, b, k) = map(int, input().split())
(s, d) = (0, [])
for (i, q) in enumerate(input(), 1):
	if q == '0':
		s += 1
		if s == b:
			d += [str(i)]
			s = 0
	else:
		s = 0
m = len(d) - a + 1
print(m, ' '.join(d[:m]))
