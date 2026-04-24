import sys, io, os
if os.environ['USERNAME'] == 'kissz':
	inp = open('in55.txt', 'r').readline

	def debug(*args):
		print(*args, file=sys.stderr)
else:
	inp = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

	def debug(*args):
		pass

def mexp(size, power):
	A = []
	for i in range(size):
		A.append([int(j <= i // 2 * 2) for j in range(size)])
	powers = {1: A}
	p = 1
	while p * 2 <= power:
		powers[p * 2] = mmmult(powers[p], powers[p])
		p *= 2
	A = powers[p]
	power -= p
	while power > 0:
		p = p // 2
		if p <= power:
			A = mmmult(A, powers[p])
			power -= p
	return A

def mvmult(A, V):
	res = []
	for i in range(len(A)):
		res.append(sum((a * v for (a, v) in zip(A[i], V))) % 998244353)
	return res

def mmmult(A, B):
	res = []
	for i in range(len(A)):
		res.append([sum((a * B[j][k] for (j, a) in enumerate(A[i]))) for k in range(len(B[0]))])
	return res

def get_rep(corners):
	corners[0] -= 1
	corners[-1] += 1
	bps = sorted(list(set(corners)))
	m = len(bps)
	X = [1]
	active = [1]
	for i in range(1, m):
		(x, y) = (bps[i - 1], bps[i])
		d = y - x
		A = mexp(len(active), d)
		X = mvmult(A, X)
		if i < m - 1:
			for (j, c) in enumerate(corners):
				if c == y:
					if j % 2:
						idx = active.index(j)
						X[idx + 2] += X[idx]
						active.pop(idx)
						active.pop(idx)
						X.pop(idx)
						X.pop(idx)
					else:
						active += [j, j + 1]
						active.sort()
						idx = active.index(j)
						X = X[:idx] + [0, X[idx - 1]] + X[idx:]
		else:
			return X[0]
n = int(inp())
inp()
(d, *D) = map(int, inp().split())
if d == 0 and all((dd == 0 for dd in D)):
	print(1, 1)
else:
	while d == 0:
		(d, *D) = D
	up = d >= 0
	corners = [0, d]
	for d in D:
		x = corners[-1] + d
		if up == (d >= 0):
			corners[-1] = x
		if up != (d >= 0):
			up = d >= 0
			corners.append(x)
	debug(corners)
	cands = [(-1, 0, 0)]
	low = (0, 0)
	maxdiff = (0, 0, 0)
	for (i, corner) in enumerate(corners):
		if corner < low[0]:
			low = (corner, i)
		if corner - low[0] >= cands[0][0]:
			if corner - low[0] == cands[0][0] and low[1] > cands[0][1]:
				cands += [(corner - low[0], low[1], i)]
			else:
				cands = [(corner - low[0], low[1], i)]
	L = cands[0][0] + 1
	if L > 1:
		X = 0
		debug(cands)
		for (_, starti, endi) in cands:
			X += get_rep(corners[starti:endi + 1])
	else:
		X = 1 - corners[-1]
	print(L, X % 998244353)
