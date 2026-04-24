d = [0] * 1000001
for _ in [0] * int(input()):
	m = c = 0
	for x in input():
		c += 2 * (x < ')') - 1
		m = min(m, c)
	d[c] += m in (0, c)
print((sum(map(min, zip(d[1:], d[::-1]))) + d[0]) // 2)
