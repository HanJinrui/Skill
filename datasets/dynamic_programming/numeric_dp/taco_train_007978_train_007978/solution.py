def main():
	zero = n = int(input())
	(r1, way) = ([(1000000, 1000000)] * n, [])
	r1[0] = (0, 0)
	for i in range(n):
		(r0, r1, rway) = (r1, [], [])
		way.append(rway)
		c2 = c5 = 1000000
		for (x, (u2, u5)) in zip(map(int, input().split()), r0):
			if c2 > u2:
				c2 = u2
				rway.append(False)
			else:
				rway.append(True)
			if c5 > u5:
				c5 = u5
				rway.append(False)
			else:
				rway.append(True)
			if x:
				while not x % 2:
					x //= 2
					c2 += 1
				while not x % 5:
					x //= 5
					c5 += 1
			else:
				c2 += 1
				c5 += 1
				zero = i
			r1.append((c2, c5))
	if zero < n and c2 and c5:
		print('1\n', 'D' * zero, 'R' * (n - 1), 'D' * (n - zero - 1), sep='')
		return
	(x, y) = (n * 2 - 2, n - 1)
	if c2 > c5:
		c2 = c5
		x += 1
	l = []
	while x > 1 or y:
		if way[y][x]:
			l.append('R')
			x -= 2
		else:
			l.append('D')
			y -= 1
	print(c2)
	print(''.join(reversed(l)))
main()
