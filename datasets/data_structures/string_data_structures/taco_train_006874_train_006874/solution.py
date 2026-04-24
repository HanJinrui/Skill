class Solution:

	def findPrefixes(self, arr, N):
		result = []
		for i in range(N):
			target = arr[i]
			s = target[0]
			k = 1
			j = 0
			while j < N:
				if arr[j][:k] == s and j != i:
					k += 1
					s = target[:k]
				else:
					j += 1
			result.append(s)
		return result
