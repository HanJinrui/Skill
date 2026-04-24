from sys import *
f = lambda : map(int, stdin.readline().split())
(n, t) = f()
m = 65
r = range(m)
p = [[0] * m for i in r]
p[1][0] = n // 4
p[0][0] = n % 4
q = k = 1
while q:
	k += 1
	q = 0
	for x in r[1:k]:
		for y in r[:x + 1]:
			if p[x][y] < 4:
				continue
			q = 1
			d = p[x][y] // 4
			p[x][y] %= 4
			p[x + 1][y] += d
			if x > y:
				if x > y + 1:
					p[x][y + 1] += d
					p[x - 1][y] += d
				else:
					p[x][x] += 2 * d
					if y:
						p[y][y] += 2 * d
					else:
						p[x][y] += d
			if y:
				p[x][y - 1] += d if y > 1 else 2 * d
s = []
for j in range(t):
	(x, y) = f()
	(x, y) = (abs(x), abs(y))
	if x < y:
		(x, y) = (y, x)
	s.append(p[x][y] if x < m else 0)
stdout.write('\n'.join(map(str, s)))
