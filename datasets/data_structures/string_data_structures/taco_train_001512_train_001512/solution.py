class Solution:

	def combine(self, n, s):
		rr = 0
		bb = 0
		rb = 0
		br = 0
		l = len(s[0])
		ans = 0
		for i in s:
			if i[0] == 'R':
				if i[-1] == 'R':
					rr += 1
				else:
					rb += 1
			elif i[-1] == 'R':
				br += 1
			else:
				bb += 1
		if rb == 0 and br == 0:
			ans = max(rr, bb)
		elif rb == br:
			ans = rr + bb + 2 * rb
		else:
			ans = rr + bb + 2 * min(rb, br) + 1
		if ans == 1:
			return 0
		return ans * l
