t = int(input())
for i in range(t):
	(n, m) = map(int, input().split())
	M = [list('X' * (m + 2))] + [list('X' + input() + 'X') for j in range(n)] + [list('X' * (m + 2))]
	k = int(input())
	(src,) = [(y, x) for y in range(n + 2) for x in range(m + 2) if M[y][x] == 'M']
	(dst,) = [(y, x) for y in range(n + 2) for x in range(m + 2) if M[y][x] == '*']
	M[src[0]][src[1]] = '.'
	M[dst[0]][dst[1]] = '.'
	q = [(src, 0)]
	while q:
		((y, x), kk) = q.pop()
		if (y, x) == dst:
			print('Impressed' if kk == k else 'Oops!')
			break
		M[y][x] = 'X'
		r = []
		for pos in [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]:
			if M[pos[0]][pos[1]] == '.':
				r.append(pos)
		if len(r) > 1:
			kk += 1
		for pos in r:
			q.append((pos, kk))
