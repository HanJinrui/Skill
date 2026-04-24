import sys
input = sys.stdin.readline

def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)

class Tree:

	def __init__(self, n):
		self.base = 1
		while self.base < n:
			self.base *= 2
		self.seg = [(0, 1)] * (2 * self.base)

	def merge(self, x, y):
		g = gcd(x[0], y[0])
		return (g, (x[1] if x[0] == g else 0) + (y[1] if y[0] == g else 0))

	def set(self, i, v):
		i += self.base
		self.seg[i] = (v, 1)
		i //= 2
		while i >= 1:
			self.seg[i] = self.merge(self.seg[2 * i], self.seg[2 * i + 1])
			i //= 2

	def get(self, l, r):
		l += self.base
		r += self.base
		res = (0, 1)
		while l <= r:
			if l % 2 == 1:
				res = self.merge(res, self.seg[l])
				l += 1
			if r % 2 == 0:
				res = self.merge(res, self.seg[r])
				r -= 1
			l //= 2
			r //= 2
		return res
n = int(input())
s = list(map(int, input().split()))
tree = Tree(n)
for i in range(n):
	tree.set(i, s[i])
t = int(input())
res = []
for _ in range(t):
	(l, r) = map(int, input().split())
	l -= 1
	r -= 1
	res.append(r - l + 1 - tree.get(l, r)[1])
print('\n'.join(map(str, res)))
