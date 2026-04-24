class Solution:

	def rotation(self, N):
		q = []
		while N > 0:
			q.append(N)
			i = 1
			while i <= N:
				q.append(q.pop(0))
				i += 1
			N -= 1
		return q[::-1]
