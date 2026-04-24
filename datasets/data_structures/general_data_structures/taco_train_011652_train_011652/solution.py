from itertools import combinations

class Solution:

	def countTriplets(self, nums):
		return sum((sum((n < num for n in nums[:index + 2])) * sum((n > num for n in nums[index + 1:])) for (index, num) in enumerate(nums[1:-1])))
