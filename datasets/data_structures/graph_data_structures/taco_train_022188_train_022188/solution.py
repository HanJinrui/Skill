class Solution:

	def avoidExlosion(self, mix, n, danger, m):
		ds = list(range(n))

		def find(a):
			if ds[a] != a:
				ds[a] = find(ds[a])
			return ds[a]
		result = []
		for (x, y) in mix:
			(x, y) = (find(x - 1), find(y - 1))
			for (p, q) in danger:
				(p, q) = (find(p - 1), find(q - 1))
				if (x, y) == (p, q) or (x, y) == (q, p):
					result.append('No')
					break
			else:
				result.append('Yes')
				ds[x] = y
		return result
