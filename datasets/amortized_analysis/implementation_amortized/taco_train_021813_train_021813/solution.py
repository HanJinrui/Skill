class Solution:

	def appleSequences(self, n, k, a):
		c = j = len = 0
		for i in range(0, n):
			if a[i] == 'O':
				c += 1
			while c > k:
				if a[j] == 'O':
					c -= 1
				j += 1
			len = max(len, i - j + 1)
		return len
