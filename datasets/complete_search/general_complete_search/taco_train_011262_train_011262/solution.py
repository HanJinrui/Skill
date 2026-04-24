class Solution:

	def shiftPile(self, N, n):
		li = []

		def rec(N, s, a, d):
			if N == 1:
				li.append([s, d])
				return
			rec(N - 1, s, d, a)
			li.append([s, d])
			rec(N - 1, a, s, d)
		rec(N, '1', '2', '3')
		return li[n - 1]
