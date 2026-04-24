class Solution:

	def findgroups(self, arr, n):
		cnts = [0] * 3
		for x in arr:
			cnts[x % 3] += 1
		ans = cnts[0] * (cnts[0] - 1) // 2 + cnts[1] * cnts[2] + cnts[0] * cnts[1] * cnts[2]
		ans += sum([cnts[x] * (cnts[x] - 1) * (cnts[x] - 2) // 6 for x in [1, 2, 0]])
		return ans
