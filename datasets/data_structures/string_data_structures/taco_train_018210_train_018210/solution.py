class Solution:

	def wordBreak(self, A, B):
		if len(A) == 0 or A in B:
			return 1
		else:
			for i in range(len(A)):
				if A[0:i] in B and self.wordBreak(A[i:], B):
					return True
			return False
