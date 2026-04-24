for _ in [0] * int(input()):
	n = int(input())
	t = [2] * n
	m = g = 0
	for (l, r, i) in sorted(([*map(int, input().split()), i] for i in range(n))):
		g += l > m
		m = max(m, r)
		t[i] -= g & 1
	print(*(t, [-1])[g < 2])
