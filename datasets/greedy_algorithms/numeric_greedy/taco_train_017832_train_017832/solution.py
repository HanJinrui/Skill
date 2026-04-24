def expand(a, m):
	b = []
	for x in a:
		t = x
		while t % m == 0:
			t //= m
		if b and b[-1][0] == t:
			b[-1][1] += x // t
		else:
			b.append([t, x // t])
	return b
for _ in range(int(input())):
	(_, m) = map(int, input().split())
	a = map(int, input().split())
	input()
	b = map(int, input().split())
	print('Yes' if expand(a, m) == expand(b, m) else 'No')
