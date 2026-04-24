class Item:

	def __init__(self, val, w):
		self.value = val
		self.weight = w

class Solution:

	def fractionalknapsack(self, W, arr, n):
		items = sorted(arr, key=lambda x: x.weight / x.value)
		result = 0
		for item in items:
			if W <= 0:
				break
			result += min(1, W / item.weight) * item.value
			W -= item.weight
		return result
