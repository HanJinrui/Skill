import numpy as np

class Solution:

	def columnWithMaxZeros(self, arr, N):
		a = np.array(arr)
		b = np.sum(a, axis=0)
		c = min(b)
		for i in range(N):
			if b[i] == c:
				return i
