class Solution:

	def find3number(self, A, n):
		(i, j, k) = (A[0], sys.maxsize - 1, A[0])
		for val in A[1:]:
			if val < i:
				i = val
			elif val > i and val < j:
				j = val
				k = i
			elif val > j:
				return [k, j, val]
		return []
