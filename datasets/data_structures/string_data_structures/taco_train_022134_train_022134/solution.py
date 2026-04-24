class Solution:

	def beautySum(self, s):
		ret = 0
		for i in range(len(s)):
			d = {}
			for j in range(i, len(s)):
				d.setdefault(s[j], 0)
				d[s[j]] += 1
				ret += max(d.values()) - min(d.values())
		return ret
