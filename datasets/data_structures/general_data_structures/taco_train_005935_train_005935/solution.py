for _ in range(int(input())):
	(x1, y1) = list(map(int, input().split()))
	(x2, y2) = list(map(int, input().split()))
	n = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
	for (dx, dy) in n:
		nx = x1 + dx
		ny = y1 + dy
		if (nx - x2, ny - y2) in n:
			if nx >= 1 and nx <= 8 and (ny >= 1) and (ny <= 8):
				print('YES')
				break
	else:
		print('NO')
