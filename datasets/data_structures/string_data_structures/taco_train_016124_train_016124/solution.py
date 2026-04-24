class Solution:

	def repeatedStringMatch(self, A, B):
		temp = A
		for i in range(1, 100):
			if B in temp:
				return i
			temp += A
		return -1
