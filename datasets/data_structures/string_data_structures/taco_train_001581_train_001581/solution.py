class Solution:

	def maxDistinctNum(self, arr, n):
		d = {}
		ans = []
		for x in arr:
			if x > 0:
				d[x] = d.get(x, 0) + 1
			elif abs(x) in d:
				num = abs(x)
				d[num] = d.get(num) - 1
				if d[num] == 0:
					del d[num]
			ans.append(len(d))
		return ans
