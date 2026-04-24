class Solution:

	def compress(self, s):
		i = len(s) - 1
		res = ''
		while i >= 0:
			if i % 2 == 1:
				mid = i // 2 + 1
				if s[0:mid] == s[mid:i + 1]:
					res += '*'
					i = mid - 1
				else:
					res += s[i]
					i = i - 1
			else:
				res += s[i]
				i = i - 1
		res = res[::-1]
		return res
