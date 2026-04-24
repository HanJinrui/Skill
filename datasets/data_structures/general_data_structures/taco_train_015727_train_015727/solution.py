import sys
M = 1000003
F = [1] * M
for i in range(1, M):
	F[i] = i * F[i - 1] % M

def f(i):
	return F[i] if i < M else 0

def build(a, i, j):
	if i + 1 == j:
		return (i, j, None, None, a[i][1], a[i][1], a[i][0], pow(a[i][0], a[i][1], M))
	l = build(a, i, (i + j) // 2)
	r = build(a, (i + j) // 2, j)
	K = l[5] + r[5]
	d = l[6] * r[6] % M
	V = l[7] * r[7] % M
	return (i, j, l, r, 0, K, d, V)

def update(t, i, j, p):
	(ti, tj, tl, tr, tp, tK, td, tV) = t
	if tj <= i or j <= ti:
		return (t, 0, 1)
	if i <= ti and tj <= j:
		tp += p
		dk = (tj - ti) * p
		dv = pow(td, p, M) if dk < M else 0
	else:
		(tl, lk, lv) = update(tl, i, j, p) if tl != None else (tl, 0, 1)
		(tr, rk, rv) = update(tr, i, j, p) if tr != None else (tr, 0, 1)
		(dk, dv) = (lk + rk, lv * rv % M)
	tK += dk
	tV = tV * dv % M
	return ((ti, tj, tl, tr, tp, tK, td, tV), dk, dv)

def queryK(t, i, j, p=0):
	(ti, tj, tl, tr, tp, tK, td, tV) = t
	if tj < i or j < ti:
		return 0
	if i <= ti and tj <= j:
		return tK + (tj - ti) * p
	lk = queryK(tl, i, j, p + tp) if tl != None else 0
	rk = queryK(tr, i, j, p + tp) if tr != None else 0
	return lk + rk

def queryV(t, i, j, p=0):
	(ti, tj, tl, tr, tp, tK, td, tV) = t
	if tj < i or j < ti:
		return 1
	if i <= ti and tj <= j:
		return tV * pow(td, p, M) % M
	lv = queryV(tl, i, j, p + tp) if tl != None else 1
	rv = queryV(tr, i, j, p + tp) if tr != None else 1
	return lv * rv % M
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split()[1:])) for i in range(n)]
T = build(a, 0, len(a))
for q in range(int(sys.stdin.readline())):
	x = list(map(int, sys.stdin.readline().split()))
	if x[0]:
		T = update(T, x[1] - 1, x[2], x[3])[0]
	else:
		k = queryK(T, x[1] - 1, x[2])
		v = queryV(T, x[1] - 1, x[2]) if k < M else 0
		print('%d %d' % (k, v * f(k) % M))
