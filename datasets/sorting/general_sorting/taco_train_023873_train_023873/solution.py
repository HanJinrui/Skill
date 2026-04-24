class Solution:

	def minimum_difference(self, nums):
		nums.sort()
		mn = min((nums[i] - nums[i - 1] for i in range(1, len(nums))))
		return mn
