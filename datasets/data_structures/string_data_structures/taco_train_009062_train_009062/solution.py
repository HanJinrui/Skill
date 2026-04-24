class Solution:

	def minManipulation(self, N, S1, S2):
		cnt = N
		for i in S1:
			if i in S2:
				cnt -= 1
				S2 = S2.replace(i, '', 1)
		return cnt
