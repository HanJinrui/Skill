class Solution:

	def secondSmallest(self, S, D):
		if D == 1 or S == 1:
			return -1
		k = S // 9
		if k >= D:
			return -1
		r = S % 9
		if r == 0:
			r = 9
			k -= 1
		if k == 0:
			return 1 * 10 ** (D - 1) + 10 + (r - 2)
		else:
			return 1 * 10 ** (D - 1) + r * 10 ** k + 9 * 10 ** (k - 1) - 1
