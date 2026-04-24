class Solution:

	def canPair(self, nums, k):
		if len(nums) % 2 == 1:
			return False
		temp = [0] * k
		for i in nums:
			n = i % k
			temp[i % k] += 1
		return temp[1:] == temp[1:][::-1] and temp[0] % 2 == 0
