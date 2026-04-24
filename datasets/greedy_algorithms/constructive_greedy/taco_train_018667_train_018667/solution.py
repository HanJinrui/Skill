from sys import stdin, stdout
n = int(stdin.readline())
points = list(map(int, stdin.readline().split()))
teams = []
chance = []
for i in range(n):
	teams.append(tuple(map(int, stdin.readline().split())))
k = int(stdin.readline())
for i in range(n):
	(f, s, t) = teams[i]
	if not k in teams[i]:
		chance += [f, s, t]
	else:
		(a, b) = [f, s, t][:[f, s, t].index(k)] + [f, s, t][[f, s, t].index(k) + 1:]
		if points.index(a) < points.index(k) or points.index(b) < points.index(k):
			chance = []
			for i in range(1, 3 * n + 1):
				if i != k:
					chance.append(i)
		else:
			chance += [a, b]
		break
chance.sort()
s = set(chance)
for i in range(1, 3 * n + 1):
	if not i in s and i != k:
		chance.append(i)
chance = chance[:chance.index(max(a, b)) + 1] + sorted(chance[chance.index(max(a, b)) + 1:])
stdout.write(' '.join(list(map(str, chance))))
