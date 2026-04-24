import sys
i = iter(([*map(int, s.split())] for s in sys.stdin))
next(i)
for ((n, k), a) in zip(i, i):
	b = ''.join(('01'[i == j] for (i, j) in zip(range(1, n + 1), a)))
	l = b.find('0')
	if l < 0:
		ans = 0
	else:
		r = b.rfind('0') + 1
		m = r - l
		if m <= k:
			ans = 1
		else:
			(*t,) = range(l + 1, r + 1)
			(i, j) = (0, k)
			for u in range(4):
				if ~u & 1:
					b = a[l:r]
				b[i:j] = sorted(b[i:j])
				if u & 1:
					if b == t:
						ans = 2
						break
				else:
					(i, j) = (m - j, m - i)
			else:
				ans = 3
	print(ans)
