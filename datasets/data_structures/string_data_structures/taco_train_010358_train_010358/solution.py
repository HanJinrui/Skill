class Solution:

	def fractionToDecimal(self, n, d):
		q = n // d
		r = n % d
		ans = str(q)
		if r == 0:
			return ans
		ans += '.'
		dic = {}
		while r != 0:
			if dic.get(r) != None:
				l = dic[r]
				ans = ans[0:l] + '(' + ans[l:] + ')'
				break
			else:
				dic[r] = len(ans)
				r = r * 10
				newQ = r // d
				r = r % d
				ans += str(newQ)
		return ans
