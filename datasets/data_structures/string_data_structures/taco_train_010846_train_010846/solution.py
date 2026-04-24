class Solution:

	def KthDistinct(self, nums, k):
		l = [0] * (max(nums) + 1)
		freq = 0
		for i in nums:
			l[i] += 1
		for i in nums:
			if l[i] == 1:
				freq += 1
			if freq == k:
				return i
		return -1
