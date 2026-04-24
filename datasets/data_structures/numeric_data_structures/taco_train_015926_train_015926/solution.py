import numpy as np

class Solution:

	def numOfsubarrays(self, arr, n):
		c = 0
		for i in range(n + 1):
			for j in range(i):
				p = arr[j:i]
				if sum(p) == np.prod(p):
					c += 1
		return c
