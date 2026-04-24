class Solution:

	def countWays(self, N):
		l = [1, 1, 2, 4]
		for i in range(4, N):
			l.append(l[-1] + l[-3] + l[-4])
			l[-1] = l[-1] % 1000000007
		return l[N - 1] % 1000000007
