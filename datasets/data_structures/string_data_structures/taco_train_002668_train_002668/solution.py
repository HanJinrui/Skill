class Solution:

	def TotalPairs(self, nums, k):
		d = set(nums)
		ans = 0
		for i in d:
			if i + k in d:
				ans += 1
		return ans
