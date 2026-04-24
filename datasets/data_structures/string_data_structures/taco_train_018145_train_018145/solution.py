class Solution:

	def concatenatedString(self, s1, s2):
		ans = ''
		ad = s1 + s2
		for i in ad:
			if i not in s1 or i not in s2:
				ans += i
		if ans == '':
			return -1
		return ans
