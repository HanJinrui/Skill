import sys
data = sys.stdin.readlines()
(n, m) = map(int, data[0].split())
g = {}
for (i, line) in enumerate(data[1:-1], 1):
	g[i] = list(map(int, line.split()[1:]))
mk = {}
start = int(data[-1])
queue = [(start, 0, -1, 1)]
cycle = False
while len(queue) > 0:
	(v, player, prev, color) = queue.pop()
	if color == 2:
		mk[v, player] = (prev, 2)
		continue
	if mk.get((v, player), None):
		if mk[v, player][1] == 1:
			cycle = True
		continue
	mk[v, player] = (prev, 1)
	queue.append((v, player, prev, 2))
	for w in g[v]:
		queue.append((w, 1 - player, v, 1))
sol = None
for v in range(1, n + 1):
	if len(g[v]) == 0 and mk.get((v, 1), None):
		sol = v
		break
if sol:
	path = [sol]
	cur = (sol, 1)
	while cur != (start, 0):
		cur = (mk.get(cur)[0], 1 - cur[1])
		path.append(cur[0])
	print('Win')
	print(*path[::-1])
elif cycle:
	print('Draw')
else:
	print('Lose')
