C = input
D = range
E = int

def N(l, r, d, ms):
	while l < r:
		if l & 1:
			d[l] += 1
			ms[l] = 0
			l += 1
		if r & 1:
			r -= 1
			d[r] += 1
			ms[r] = 0
		l >>= 1
		r >>= 1

def O(ms, d, c):
	for A in ms:
		A >>= 1
		while A:
			B = A << 1
			C = B + 1
			D = d[B] + c[B]
			E = d[C] + c[C]
			F = D if D > E else E
			if F <= c[A]:
				break
			c[A] = F
			A >>= 1

def P(node, c):
	A = node
	A >>= 1
	while A:
		B = A << 1
		F = B + 1
		C = c[B]
		D = c[F]
		E = C if C > D else D
		if E <= c[A]:
			break
		c[A] = E
		A >>= 1
X = E(C())
I = {}
J = {}
Q = [[] for A in D(10 ** 5)]
for e in D(X):
	R = C().split()
	Y = E(R[0])
	S = E(R[1])
	Z = C().split()
	a = [E(A) for A in C().split()]
	b = [E(A) for A in C().split()]
	A = Y + 1
	for K in D(S):
		L = a[K]
		T = b[K]
		if T > L:
			Q[T].append(L if Z[K] in 'CE' else -L)
	F = [0] * (A << 1)
	B = [*F]
	U = [*F]
	H = [*F]

	def c(sl, zi):
		for E in sl:
			if E > 0:
				N(A, A + E + 1, F, I)
			else:
				N(A, A + -E + 1, U, J)
		O(I.keys(), F, B)
		O(J.keys(), U, H)
		D = B[1]
		G = H[1]
		C = A + zi
		if D ^ G:
			if D > G:
				H[C] = B[C] = D
				P(C, H)
			else:
				B[C] = G
				P(C, B)
		else:
			B[C] = D
		sl.clear()
		I.clear()
		J.clear()
	for G in D(1, A):
		V = Q[G]
		if V:
			c(V, G)
	W = [-1] * S
	M = 0
	for G in D(1, A):
		d = G + A
		while M < B[d]:
			W[M] = G
			M += 1
	print(*W)
