import itertools
import math
(N, x, y) = [int(n) for n in input().split()]
pills = []
for i in range(N):
	pills.append(tuple((int(n) for n in input().split())) + (i + 1,))
pills.sort()
rques = x
qauto = 0
time = 0
used = []
possible = set()
while rques > 0:
	while len(pills) > 0 and pills[-1][0] >= 100 * rques / x:
		possible.add(pills.pop()[1:])
	if len(possible) > 0:
		best = max(possible)
		used.append((best, time))
		possible.remove(best)
		qauto += best[0]
	elif qauto <= y:
		print('NO')
		break
	rques = min(rques + y - qauto, x)
	time += 1
else:
	print('YES')
	print(time, len(used))
	for scroll in used:
		print(scroll[1], scroll[0][1])
