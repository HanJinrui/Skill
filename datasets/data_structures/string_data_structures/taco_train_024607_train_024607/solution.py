from collections import Counter

class Solution:

	def transfigure(self, A, B):
		if Counter(A) != Counter(B):
			return -1
		i = j = len(A) - 1
		while i >= 0:
			if A[i] == B[j]:
				j -= 1
			i -= 1
		return j + 1
