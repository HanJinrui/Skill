import sys, io, os
try:
	Z = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
except:
	Z = lambda : sys.stdin.readline().encode()
from math import atan2
from collections import deque

def path(R):
	H = deque()
	H.append(R)
	while P[R] >= 0:
		R = P[R]
		H.append(R)
		if len(H) > 2:
			P[H.popleft()] = H[-1]
	return R

def remove_middle(a, b, c):
	cross = (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])
	dot = (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1])
	return cross < 0 or (cross == 0 and dot <= 0)

def convex_hull(points):
	spoints = sorted(points)
	hull = []
	for p in spoints + spoints[::-1]:
		while len(hull) >= 2 and remove_middle(hull[-2], hull[-1], p):
			hull.pop()
		hull.append(p)
	hull.pop()
	return hull
n = int(Z())
p = []
p2 = []
w = [-1] * n
labels = set()
for i in range(n):
	(x, y, a) = map(int, Z().split())
	a -= 1
	if a != i:
		p.append((x, y, i))
		p2.append((x, y))
		w[i] = a
		labels.add(a)
if not p:
	print(0)
	quit()
q = []
(bx, by, bi) = p[-1]
L = len(p) - 1
for i in range(L):
	(x, y, l) = p[i]
	q.append((atan2(y - by, x - bx), (x, y), l))
q.sort()
cycles = [-1] * n
c = 0
while labels:
	v = labels.pop()
	cycles[v] = c
	cur = w[v]
	while cur != v:
		labels.remove(cur)
		cycles[cur] = c
		cur = w[cur]
	c += 1
K = [-1] * c
P = [-1] * c
S = [1] * c
R = 0
moves = []
ch = convex_hull(p2)
adj1 = adj2 = None
for i in range(len(ch)):
	(x, y) = ch[i]
	if x == bx and y == by:
		adj1 = ch[(i + 1) % len(ch)]
		adj2 = ch[i - 1]
		break
for i in range(L):
	if q[i][1] == adj1 and q[i - 1][1] == adj2 or (q[i][1] == adj2 and q[i - 1][1] == adj1):
		continue
	(l1, l2) = (q[i][2], q[i - 1][2])
	(a, b) = (cycles[l1], cycles[l2])
	if a != b:
		if K[a] >= 0:
			if K[b] >= 0:
				(va, vb) = (path(K[a]), path(K[b]))
				if va != vb:
					moves.append((l1, l2))
					(sa, sb) = (S[va], S[vb])
					if sa > sb:
						P[vb] = va
					else:
						P[va] = vb
						if sa == sb:
							S[vb] += 1
				else:
					pass
			else:
				K[b] = path(K[a])
				moves.append((l1, l2))
		elif K[b] >= 0:
			K[a] = path(K[b])
			moves.append((l1, l2))
		else:
			K[a] = R
			K[b] = R
			R += 1
			moves.append((l1, l2))
for (a, b) in moves:
	(w[a], w[b]) = (w[b], w[a])
while w[bi] != bi:
	a = w[bi]
	b = w[a]
	moves.append((a, bi))
	(w[bi], w[a]) = (b, a)
print(len(moves))
print('\n'.join((f'{a + 1} {b + 1}' for (a, b) in moves)))
