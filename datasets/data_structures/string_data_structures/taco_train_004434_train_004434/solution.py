class Solution:

	def transform(self, A, B):
		res = 0
		if len(A) != len(B) or sorted(A) != sorted(B):
			return -1
		j = len(B) - 1
		for ch in A[::-1]:
			if ch != B[j]:
				res += 1
			else:
				j -= 1
		return res
