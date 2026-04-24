class Solution:

	def sameChar(self, A, B):
		num = 0
		for (i, s) in enumerate(A):
			if s.lower() == B[i].lower():
				num += 1
		return num
