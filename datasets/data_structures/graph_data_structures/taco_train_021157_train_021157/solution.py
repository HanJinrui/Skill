import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
(same, both) = (0, 0)
edges = {}
for _ in range(m):
	x = input().split()
	if x[0] == '+':
		(k, i, j, c) = x
		edges[i, j] = c
		if (j, i) in edges:
			both += 1
			same += edges[j, i] == c
	elif x[0] == '-':
		(k, i, j) = x
		if (j, i) in edges:
			both -= 1
			same -= edges[i, j] == edges[j, i]
		del edges[i, j]
	else:
		i = int(x[1])
		if not i % 2:
			print('YES' if same else 'NO')
		else:
			print('YES' if both else 'NO')
