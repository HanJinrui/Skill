for _ in range(int(input())):
	s = input()
	p = int(input())
	a = sorted([(ord(x) - 96, i) for (i, x) in enumerate(s)])
	m = sum((x for (x, i) in a))
	while m > p:
		t = a.pop()
		m -= t[0]
	print(''.join((chr(x + 96) for (x, i) in sorted(a, key=lambda tup: tup[1]))))
