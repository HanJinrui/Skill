class Solution:

	def countCarry(self, A, B):
		c = 0
		p = 0
		while A and B:
			d1 = A % 10
			d2 = B % 10
			c = (d1 + d2 + c) // 10
			if c > 0:
				p += 1
			A //= 10
			B //= 10
		return p
