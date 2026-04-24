import sys
readline = sys.stdin.readline
from collections import defaultdict

class UnionFind:

	def __init__(self, n):
		self.n = n
		self.parents = [-1] * n

	def Find(self, x):
		stack = []
		while self.parents[x] >= 0:
			stack.append(x)
			x = self.parents[x]
		for y in stack:
			self.parents[y] = x
		return x

	def Union(self, x, y):
		x = self.Find(x)
		y = self.Find(y)
		if x == y:
			return
		if self.parents[x] > self.parents[y]:
			(x, y) = (y, x)
		self.parents[x] += self.parents[y]
		self.parents[y] = x

	def Size(self, x):
		return -self.parents[self.Find(x)]

	def Same(self, x, y):
		return self.Find(x) == self.Find(y)

	def Members(self, x):
		root = self.Find(x)
		return [i for i in range(self.n) if self.Find(i) == root]

	def Roots(self):
		return [i for (i, x) in enumerate(self.parents) if x < 0]

	def Group_Count(self):
		return len(self.Roots())

	def All_Group_Members(self):
		group_members = defaultdict(list)
		for member in range(self.n):
			group_members[self.Find(member)].append(member)
		return group_members

	def __str__(self):
		return '\n'.join((f'{r}: {m}' for (r, m) in self.All_Group_Members().items()))
T = int(readline())
for _ in range(T):
	(N, M) = map(int, readline().split())
	UF = UnionFind(2 * N)
	edges = []
	for _ in range(M):
		(x, y) = map(int, readline().split())
		x -= 1
		y -= 1
		edges.append((x, y))
	W = int(readline())
	se = set(map(int, readline().split()))
	for i in range(M):
		if not i + 1 in se:
			(x, y) = edges[i]
			UF.Union(x, y + N)
			UF.Union(x + N, y)
	ans = 'YES'
	for x in range(N):
		if UF.Same(x, x + N):
			ans = 'NO'
	print(ans)
