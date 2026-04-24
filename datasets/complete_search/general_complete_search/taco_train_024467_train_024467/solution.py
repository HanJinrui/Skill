g = [0, 1, 2]
for n in range(3, 301):
	s = set()
	for l in (1, 2):
		for i in range((n - l) // 2 + 1):
			s.add(g[i] ^ g[n - l - i])
	m = 0
	while m in s:
		m += 1
	g.append(m)
for _ in range(int(input())):
	input()
	r = 0
	for p in input().split('X'):
		r ^= g[len(p)]
	print('WIN' if r else 'LOSE')
