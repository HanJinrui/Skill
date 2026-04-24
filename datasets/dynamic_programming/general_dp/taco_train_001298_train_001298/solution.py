class Solution:

	def AlternatingaMaxLength(self, nums):
		x = 1
		y = 1
		for i in range(1, n):
			if nums[i] < nums[i - 1]:
				x = y + 1
			elif nums[i] > nums[i - 1]:
				y = x + 1
		return max(x, y)
