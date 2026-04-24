class Solution:

	def productExceptSelf(self, nums, n):
		res = [1] * n
		pre = 1
		post = 1
		for i in range(n):
			res[i] *= pre
			pre *= nums[i]
		for i in range(n - 1, -1, -1):
			res[i] *= post
			post *= nums[i]
		return res
