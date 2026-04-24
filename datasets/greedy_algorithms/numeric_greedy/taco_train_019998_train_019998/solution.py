class Solution:

	def digitsNum(self, N):
		return int(str(N % 9) + '9' * (N // 9)) * pow(10, N)
