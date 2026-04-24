class Solution:

	def findRange(self, s, n):
		cmax = cnt = 0
		l = r = 1
		ans = [-1]
		for i in range(n):
			cnt += 1 if s[i] == '0' else -1
			if cnt > cmax:
				cmax = cnt
				r = i + 1
				ans = (l, r)
			if cnt < 0:
				cnt = 0
				l = i + 2
		return ans
