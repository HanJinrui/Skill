class Solution:

	def isSquare(self, S):
		num = sum([ord(item) for item in S]) ** 0.5
		return int(num == int(num))
