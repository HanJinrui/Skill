def precompute():
	pass

def helpSanta(n, m, g):
	if m == 0:
		return -1
	parent = list(range(n))
	rank = [1] * n

	def find(n):
		if parent[n] != n:
			parent[n] = find(parent[n])
		return parent[n]

	def union(a, b):
		(x, y) = (find(a), find(b))
		if x == y:
			return False
		if rank[x] > rank[y]:
			parent[y] = x
			rank[x] += rank[y]
		else:
			parent[x] = y
			rank[y] += rank[x]
		return True
	for i in range(m):
		(a, b) = g[i]
		union(a - 1, b - 1)
	maxi = max(rank)
	sz = maxi * 20
	sieve = [True] * (sz + 1)
	for i in range(2, sz + 1):
		if sieve[i]:
			for j in range(i * i, sz + 1, i):
				sieve[j] = False
			maxi -= 1
			if maxi == 0:
				return i
