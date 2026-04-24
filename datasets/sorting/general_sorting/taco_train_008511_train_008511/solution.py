import sys
Z = sys.stdin.readline

def P(d=1, x=0):
	print('?', x, 2 * d - 1)
	sys.stdout.flush()
	return int(Z())

def poke(n):
	global K, S, C, L
	h = len(S)
	l = 0
	D = [0] * h
	while h - l > 1:
		m = (l + h) // 2
		d = 1 - D[l]
		for i in range(m - l):
			v = P(d, S[l + i])
			D[l + i] = d
		if v < P() + n:
			if d:
				l = m
			else:
				h = m
		elif d:
			h = m
		else:
			l = m
		P(0)
	for i in range(len(S)):
		if D[i]:
			P(0, S[i])
	for i in range(M):
		v = P(0, S[l])
	K[S[l]] = C
	L = C
	S = S[:l] + S[l + 1:]
	return v
(N, M) = map(int, Z().split())
if N == 2:
	while P() > 0:
		pass
	print('!', M)
	quit()
K = [-1] * N
S = [*range(1, N)]
pv = P()
v = P()
w = 0
while 1 - w or pv <= v:
	(pv, v, w) = (v, P(), max(w, v >= pv))
(pv, v) = (v, P(0))
good = []
for i in S:
	(pv, v) = (v, P(1, i))
	if v < pv:
		(pv, v) = (v, P())
		if v >= pv:
			good.append(i)
			P(0, i)
			K[i] = 0
		(pv, v) = (v, P(0))
for i in good:
	S.remove(i)
L = C = 0
for i in range(len(S)):
	n = 0
	while (C - L) % (N * M) < M:
		(pv, v, C) = (v, P(), C + 1)
		if pv == v:
			n = 1
			break
	else:
		pv = v
		while pv == v:
			(pv, v, C) = (v, P(), C + 1)
	P(0)
	C -= 1
	v = poke(n)
print('!', ' '.join(map(str, [(K[i] - C) % (M * N) for i in range(1, N)])))
