n = int(input())
maze = [input().strip() for _ in range(n)]

def go(by_row):
	global maze
	maze = list(zip(*maze))
	can = True
	for i in range(n):
		if '.' not in maze[i]:
			can = False
	if can:
		for i in range(n):
			for j in range(n):
				if maze[i][j] == '.':
					print(i + 1, j + 1) if by_row else print(j + 1, i + 1)
					break
	return can
if not go(0) and (not go(1)):
	print(-1)
