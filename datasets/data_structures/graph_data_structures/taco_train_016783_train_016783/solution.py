class Solution:

	def criticalConnections(self, n, x):
		t = 0
		se = set()
		v = set()
		disc = {}
		low = {}

		def f(i, p=-1):
			nonlocal t
			t += 1
			disc[i] = t
			low[i] = t
			v.add(i)
			child = 0
			for j in x[i]:
				if j != p:
					if j not in v:
						f(j, i)
						low[i] = min(low[i], low[j])
						if low[j] > disc[i]:
							se.add((min(i, j), max(i, j)))
					else:
						low[i] = min(low[i], disc[j])
		for i in range(n):
			if i not in v:
				f(i)
		return sorted(list(se))
