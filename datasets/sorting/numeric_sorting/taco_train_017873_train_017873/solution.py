for _ in range(int(input())):
	n = int(input())
	t = 2 * n
	s = 0
	l = list(map(int, input().split()))
	q = set(l)
	if 2 * len(q) != t:
		print('NO')
		continue
	l = sorted(q, reverse=True)[:n]
	j = None
	for k in l:
		p = k - s
		if p <= 0 or p % t != 0:
			print('NO')
			break
		j = p // t
		s += 2 * j
		t -= 2
	else:
		print('YES')
