import bisect
(n, m) = [int(x) for x in input().split()]
Board = [(m + 1) * [0]]
Wrong = [(m + 1) * [0]]
for i in range(n):
	row = [0] + [int(x) for x in input()]
	comRow = [0]
	for j in range(m):
		comRow.append(comRow[j] + Wrong[i][j + 1] - Wrong[i][j] + (i + j + row[j + 1]) % 2)
	Board.append(row)
	Wrong.append(comRow)
boardSize = [0] + min(n, m) * [n * n]
for k in range(len(boardSize)):
	for i in range(1, n + 1 - k):
		for j in range(1, m + 1 - k):
			changes = Wrong[i + k][j + k] - Wrong[i - 1][j + k] - Wrong[i + k][j - 1] + Wrong[i - 1][j - 1]
			boardSize[k] = min(boardSize[k], changes, (k + 1) * (k + 1) - changes)
q = int(input())
qu = [int(x) for x in input().split()]
for c in qu:
	print(min(bisect.bisect_right(boardSize, c), min(m, n)))
