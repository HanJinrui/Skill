class Solution:

	def catchThieves(self, A, n, k):
		caught = [False] * len(A)
		i = j = 0
		while j < len(A):
			if caught[i]:
				i += 1
			elif j - i < k and A[i] == A[j]:
				j += 1
			else:
				caught[j] = A[i] != A[j]
				i += 1
				j += 1
		return sum(caught)
