from sys import stdin
(x, y, n, d) = [int(x) for x in stdin.readline().split()]
d = d ** 2
v = []
for vec in range(n):
	v.append([int(x) for x in stdin.readline().split()])
found = {}

def winner(x, y, v, d):
	if x ** 2 + y ** 2 > d:
		return 1
	if (x, y) in found:
		return found[x, y]
	for (a, b) in v:
		if winner(x + a, y + b, v, d) == 0:
			found[x, y] = 1
			return 1
	found[x, y] = 0
	return 0
if winner(x, y, v, d):
	print('Anton')
else:
	print('Dasha')
