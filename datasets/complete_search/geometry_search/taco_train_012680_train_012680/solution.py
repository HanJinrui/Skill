from itertools import permutations as p
l = [list(map(int, input().split())) + [_] for _ in range(1, 9)]

def dist(a, b):
	return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def rect(a, b, c, d):
	return dist(a, b) == dist(c, d) and dist(a, c) == dist(b, d) and (dist(a, d) == dist(b, c)) and (dist(a, b) * dist(b, c) != 0)

def sq(a, b, c, d):
	return rect(a, b, c, d) and dist(a, b) == dist(b, c)
for t in p(l):
	if sq(*t[:4]) and rect(*t[4:]):
		print('YES')
		print(' '.join([str(_[2]) for _ in t[:4]]))
		print(' '.join([str(_[2]) for _ in t[4:]]))
		exit()
print('NO')
