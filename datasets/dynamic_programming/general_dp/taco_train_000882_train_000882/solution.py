import numpy

class Solution:

	def DivisibleByM(self, nums, m):
		n = len(nums)
		for i in range(n):
			for j in range(i, n):
				for k in range(j, n):
					if sum(nums[j:k + 1]) % m == 0:
						return 1
		return 0
