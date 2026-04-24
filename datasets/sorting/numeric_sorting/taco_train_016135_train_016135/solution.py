class Solution:

	def trailing_zeros(self, n):
		num = 1
		res = 0
		while num:
			ans = 0
			i = 1
			power = 5 ** i
			while power <= num:
				ans += num // power
				i += 1
				power = 5 ** i
			if ans == n:
				res += 1
			elif ans > n:
				break
			num += 1
		return res

	def countZeroes(self, n):
		return self.trailing_zeros(n)
