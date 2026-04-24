(N, M) = map(int, input().split())
(*A,) = map(int, input().split())

def gcd(m, n):
	r = m % n
	return gcd(n, r) if r else n
blk = [0] * N
F = [0] * N
(*p,) = range(N)

def root(x):
	if p[x] == x:
		return x
	z = p[x]
	p[x] = y = root(p[x])
	if F[z]:
		F[x] ^= 1
		A[x] = -A[x]
	return y

def unite(x, y):
	px = root(x)
	py = root(y)
	if px < py:
		if blk[py]:
			blk[px] = 1
		assert A[py] >= 0 and F[py] == 0
		if A[x] * A[y] >= 0:
			A[py] = -A[py]
			F[py] ^= 1
		p[py] = px
	else:
		if blk[px]:
			blk[py] = 1
		assert A[px] >= 0 and F[px] == 0
		if A[x] * A[y] >= 0:
			A[px] = -A[px]
			F[px] ^= 1
		p[px] = py
ans = []
for i in range(M):
	(T, *CS) = map(int, input().split())
	if T == 1:
		(X, C) = CS
		X -= 1
		if A[X] >= 0:
			A[X] = C
		else:
			A[X] = -C
	elif T == 2:
		(X, Y) = CS
		X -= 1
		Y -= 1
		if root(X) == root(Y):
			if A[X] * A[Y] >= 0:
				blk[root(X)] = 1
		else:
			unite(X, Y)
	else:
		(X, Y, V) = CS
		X -= 1
		Y -= 1
		if root(X) != root(Y):
			ans.append('0')
			continue
		if blk[root(X)]:
			ans.append('0')
			continue
		root(X)
		root(Y)
		a = A[X] * V
		b = A[Y]
		if b < 0:
			a = -a
			b = -b
		g = gcd(abs(a), abs(b))
		ans.append('%d/%d' % (a // g, b // g))
print(*ans, sep='\n')
