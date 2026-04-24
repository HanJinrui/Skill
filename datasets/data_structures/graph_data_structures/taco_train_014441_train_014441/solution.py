class Solution:

	def nodeLevel(self, n, x, R):
		q = [(0, 0)]
		v = {(0, 0)}
		while q:
			(i, k) = q.pop(0)
			if i == R:
				return k
			for j in x[i]:
				if j not in v:
					v.add(j)
					q.append((j, k + 1))
		return -1
