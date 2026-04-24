class Solution:

	def findDuplicate(self, arr, N, K):
		arr.sort()
		for i in arr:
			if arr.count(i) == K:
				return i
