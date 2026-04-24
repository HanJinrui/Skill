from functools import lru_cache

class Solution:

	def TotalCount(self, s):

		@lru_cache(maxsize=None)
		def cal(i, summ):
			if i == len(s):
				return 1
			ans = 0
			csum = 0
			for k in range(i, len(s)):
				csum += int(s[k])
				if csum >= summ:
					ans += cal(k + 1, csum)
			return ans
		return cal(0, 0)
