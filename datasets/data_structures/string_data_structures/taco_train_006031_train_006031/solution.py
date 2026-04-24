class Solution:

	def isSubSequence(self, A, B):
		for i in A:
			if i in B:
				B = B[B.index(i) + 1:]
			else:
				return False
		return True
