class Solution:

	def firstMissingPositive(self, nums):
		nums = sorted(set(nums), key=lambda x: x)
		result = 0
		for i in range(len(nums)):
			if nums[i] <= 0:
				continue
			elif nums[i] == result + 1:
				result += 1
			else:
				break
		return result + 1
