R = lambda : map(int, input().split())
(t,) = R()
for _ in [0] * t:
	(n, m) = R()
	s = input()
	p = sorted(R()) + [n, 0]
	r = [0] * 26
	i = j = 0
	for x in s:
		i += 1
		r[ord(x) - 97] += m + 1 - j
		while i == p[j]:
			j += 1
	print(*r)
