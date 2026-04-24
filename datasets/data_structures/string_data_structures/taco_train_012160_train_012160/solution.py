class Solution:

	def findSubarraySum(self, arr, n, k):
		cur = 0
		res = 0
		count = {0: 1}
		for i in range(n):
			cur += arr[i]
			res += count.get(cur - k, 0)
			count[cur] = count.get(cur, 0) + 1
		return res
