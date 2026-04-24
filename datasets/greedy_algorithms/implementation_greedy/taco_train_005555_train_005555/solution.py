input()
p = m = c = 0
for x in [*map(int, input().split()), 1001]:
	c = (0, c + 1)[p + 1 == x]
	m = max(m, c - 1)
	p = x
print(m)
