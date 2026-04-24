class Solution:

	def countStrings(self, S):
		l = [0] * 26
		n = len(S)
		for i in S:
			l[ord(i) - 97] += 1
		ans = 0
		for i in S:
			ans += n - l[ord(i) - 97]
		ans //= 2
		for i in l:
			if i >= 2:
				ans += 1
				break
		return ans
