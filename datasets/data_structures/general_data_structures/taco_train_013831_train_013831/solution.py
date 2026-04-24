from heapq import heappush, heappop

class Solution:

	def countArray(self, a, n):
		(ans, best) = ([-1], -1)
		(m, q) = ([0] * (n + 1), [])
		for i in range(n - 1, -1, -1):
			m[i] = max(a[i], m[i + 1])
		for (i, x) in enumerate(a):
			while q and q[0] < x and (x < m[i + 1]):
				t = q[0] * x * m[i + 1]
				if t > best:
					best = t
					ans = [q[0], x, m[i + 1]]
				heappop(q)
			heappush(q, x)
		return ans
