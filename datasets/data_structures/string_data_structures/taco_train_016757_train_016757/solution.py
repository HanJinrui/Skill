class Solution:

	def idToShortURL(self, n):
		dic = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		s = ''
		while n:
			s += dic[n % 62]
			n //= 62
		return s[::-1]
