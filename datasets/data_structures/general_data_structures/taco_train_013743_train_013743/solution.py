import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
a = list(map(int, input().split()))

class st:

	def __init__(self, size):
		N = 1
		h = 0
		while N < size:
			N <<= 1
			h += 1
		self.N = N
		self.h = h
		self.t = [float('inf')] * (2 * N)
		self.d = [0] * N

	def apply(self, p, value):
		self.t[p] += value
		if p < self.N:
			self.d[p] += value

	def build(self, p):
		t = self.t
		d = self.d
		while p > 1:
			p >>= 1
			t[p] = min(t[p << 1], t[p << 1 | 1]) + d[p]

	def rebuild(self):
		t = self.t
		for p in reversed(range(1, self.N)):
			t[p] = min(t[p << 1], t[p << 1 | 1])

	def push(self, p):
		d = self.d
		for s in range(self.h, 0, -1):
			i = p >> s
			if d[i] != 0:
				self.apply(i << 1, d[i])
				self.apply(i << 1 | 1, d[i])
				d[i] = 0

	def inc(self, l, r, value):
		if l >= r:
			return
		l += self.N
		r += self.N
		(l0, r0) = (l, r)
		while l < r:
			if l & 1:
				self.apply(l, value)
				l += 1
			if r & 1:
				r -= 1
				self.apply(r, value)
			l >>= 1
			r >>= 1
		self.build(l0)
		self.build(r0 - 1)

	def query(self, l, r):
		if l >= r:
			return float('inf')
		t = self.t
		l += self.N
		r += self.N
		self.push(l)
		self.push(r - 1)
		res = float('inf')
		while l < r:
			if l & 1:
				res = min(res, t[l])
				l += 1
			if r & 1:
				r -= 1
				res = min(t[r], res)
			l >>= 1
			r >>= 1
		return res
se = st(n)
N = se.N
for i in range(n):
	se.t[i + N] = a[i]
se.rebuild()
q = int(input())
for i in range(q):
	b = list(map(int, input().split()))
	if len(b) == 2:
		l = b[0]
		r = b[1]
		if l > r:
			print(min(se.query(l, n), se.query(0, r + 1)))
		else:
			print(se.query(l, r + 1))
	else:
		l = b[0]
		r = b[1]
		v = b[2]
		if l > r:
			se.inc(0, r + 1, v)
			se.inc(l, n, v)
		else:
			se.inc(l, r + 1, v)
