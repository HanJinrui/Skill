class Solution:

	def unitDigit(self, N, P):
		return int(N[-1] == str(int(N) ** P % 10))
