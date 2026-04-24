import sys, bisect
for _ in range(int(sys.stdin.readline())):
	(n, q) = [int(i) for i in sys.stdin.readline().split()]
	s = sys.stdin.readline()
	r = [0] * (n + 1)
	d = {}
	for i in range(n):
		x = r[i + 1] = r[i] + ((s[i] == '-') * 2 - 1) * (i % 2 * 2 - 1)
		if x in d:
			d[x].append(i)
		else:
			d[x] = [i]
	for i in range(q):
		(a, b) = [int(x) for x in sys.stdin.readline().split()]
		t = r[b] - r[a - 1]
		if t % 2:
			p = d[r[a - 1] + (t // 2 + (t > 0))]
			sys.stdout.write('1\n%d\n' % (p[bisect.bisect_left(p, a - 1)] + 1))
		elif t == 0:
			sys.stdout.write('0\n')
		else:
			t = r[b] - r[a]
			p = d[r[a] + (t // 2 + (t > 0))]
			sys.stdout.write('2\n%d %d\n' % (a, p[bisect.bisect_left(p, a)] + 1))
