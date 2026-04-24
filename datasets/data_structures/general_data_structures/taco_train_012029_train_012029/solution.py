class Solution:

	def distributeGift(self, arr, n):
		gg = {}
		ans = []
		for i in arr:
			for j in i:
				if j not in gg:
					gg[j] = 1
					ans.append(j)
					break
		return ans
