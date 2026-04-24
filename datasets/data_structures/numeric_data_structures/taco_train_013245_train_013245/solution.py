class Solution:

	def __init__(self, nums):
		self.nums = nums

	def pick(self, target):
		return random.choice([i for (i, v) in enumerate(self.nums) if v == target])
