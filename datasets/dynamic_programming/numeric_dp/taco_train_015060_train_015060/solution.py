M = 10 ** 9 + 7

class Solution:

	def countFriendsPairings(self, n):
		(a0, a1) = (1, 1)
		for i in range(2, n + 1):
			(a0, a1) = (a1, ((i - 1) * a0 % M + a1) % M)
		return a1
