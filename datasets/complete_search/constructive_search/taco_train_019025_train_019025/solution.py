for Queen in range(int(input())):
	(x, y) = map(int, input().split())
	(x, y) = (x - 1, y - 1)
	l = []
	for i in range(8):
		l.append([0] * 8)
	l[x][y] = 1
	if x == 0 and y == 0:
		l[2][1] = 2
	elif x == 7 and y == 0:
		l[6][2] = 2
	elif x == 0 and y == 7:
		l[2][6] = 2
	elif x == 7 and y == 7:
		l[6][5] = 2
	elif x == 0:
		l[2][y + 1] = 2
		l[2][y - 1] = 2
	elif y == 0:
		l[x + 1][2] = 2
		l[x - 1][2] = 2
	elif x == 7:
		l[5][y + 1] = 2
		l[5][y - 1] = 2
	elif y == 7:
		l[x + 1][5] = 2
		l[x - 1][5] = 2
	elif x > 2 and y > 2:
		l[x + 1][y - 2] = 2
		l[x - 3][y + 1] = 2
	elif x < 3 and y < 3:
		l[x - 1][y + 2] = 2
		l[x + 3][y - 1] = 2
	elif y > 2 and x < 3:
		l[x - 1][y - 2] = 2
		l[x + 3][y + 1] = 2
	elif y < 3 and x > 2:
		l[x + 1][y + 2] = 2
		l[x - 3][y - 1] = 2
	for i in l:
		print(*i)
