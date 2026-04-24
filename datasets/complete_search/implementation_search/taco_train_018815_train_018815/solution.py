mat = []
for i in range(10):
	li = list(input())
	mat.append(li)
d = [(1, 0), (0, 1), (1, 1), (1, -1)]
for i in range(10):
	for j in range(10):
		for (dx, dy) in d:
			c = 0
			t = 0
			for k in range(5):
				row = i + dx * k
				col = j + dy * k
				if row < 10 and row >= 0 and (col < 10) and (col >= 0):
					if mat[row][col] == 'X':
						c += 1
					elif mat[row][col] == '.':
						t += 1
			if c == 4 and t == 1:
				print('YES')
				exit()
print('NO')
