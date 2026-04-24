class Solution:

	def findLastOccurence(self, A, B):
		i = A.rfind(B)
		return -1 if i == -1 else i + 1
