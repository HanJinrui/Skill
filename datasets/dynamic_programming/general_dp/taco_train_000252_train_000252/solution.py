class Solution:

	def DistinctSum(self, nums):
		s = {0}
		for i in nums:
			s.update([i + j for j in s])
		return sorted(s)
