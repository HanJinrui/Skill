def init(R, x, p):
	T = [R]
	while len(R) > 1:
		if len(R) & 1:
			R.append(0)
		R = [(R[i] + x * R[i + 1]) % p for i in range(0, len(R), 2)]
		x = x * x % p
		T.append(R)
	return T

def update(T, i, x, p):
	S = T[0]
	for j in range(1, len(T)):
		R = T[j]
		i >>= 1
		R[i] = (S[2 * i] + x * S[2 * i + 1]) % p
		S = R
		x = x * x % p

def query(T, i, x, p):
	if i == 0:
		return T[-1][0]
	s = 0
	y = 1
	for j in range(len(T) - 1):
		if i & 1:
			s = (s + y * T[j][i]) % p
			y = y * x % p
		i = i + 1 >> 1
		x = x * x % p
	return s
p = 10 ** 9 + 7
(n, a, b, q) = map(int, input().split())
c = [int(x) for x in input().split()]
x = -b * pow(a, p - 2, p) % p
T = init(c, x, p)
for Q in range(q):
	(k, a, b) = map(int, input().split())
	if k == 1:
		c[a] = b
		update(T, a, x, p)
	elif k == 2:
		y = (query(T, a, x, p) - query(T, b + 1, x, p) * pow(x, b - a + 1, p)) % p
		print('No' if y else 'Yes')
