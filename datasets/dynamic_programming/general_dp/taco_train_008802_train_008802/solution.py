import sys
from operator import itemgetter
N = int(input())
(V, P) = ([None] * N, [None] * N)
for i in range(N):
	(v_item, p_item) = input().split()
	V[i] = int(v_item)
	P[i] = int(p_item)
games = []
for i in range(N):
	maxVal = -1
	games.sort(key=itemgetter(1))
	for j in range(len(games) - 1, -1, -1):
		game = games[j]
		if game[1] == 0:
			del games[0:j + 1]
			break
		if maxVal < game[0]:
			maxVal = game[0]
		else:
			del games[j]
		game[0] += V[i]
		game[1] += -1
	if maxVal == -1:
		maxVal = 0
	games.append([maxVal, P[i]])
print(max(games, key=itemgetter(0))[0])
