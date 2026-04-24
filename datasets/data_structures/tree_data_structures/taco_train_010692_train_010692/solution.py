class Solution:

	def kLevelSum(self, K, S):
		layer = 0
		ans = 0
		val = 0
		K += 1
		for i in S:
			if i == '(':
				if layer == K:
					ans += val
				layer += 1
				val = 0
			elif i == ')':
				layer -= 1
			else:
				val = int(i) + val * 10
		return ans
