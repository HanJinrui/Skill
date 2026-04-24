R = int(input())
C = int(input())

def dive(r, c):
	if G[r][c] == '0' or G[r][c] == 'X':
		return 0
	G[r][c] = 'X'
	return 1 + sum([dive(r + i, c + j) for i in range(-1, 2) for j in range(-1, 2)])
G = [['0'] * (C + 2)]
G += [['0'] + input().split() + ['0'] for _ in range(R)]
G += [['0'] * (C + 2)]
zones = []
for (r, row) in enumerate(G):
	for (c, val) in enumerate(row[:-1]):
		if val == '1' and G[r][c] != 'X':
			zones.append(dive(r, c))
print(max(zones))
