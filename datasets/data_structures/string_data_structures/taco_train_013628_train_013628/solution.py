t = int(input())
for _ in range(0, t):
	a = list(input())
	b = list(input())
	winner = 'B'
	for c in a:
		if a.count(c) > 1 and c not in b:
			winner = 'A'
			break
	if winner == 'B' and set(b) < set(a):
		winner = 'A'
	print(winner)
