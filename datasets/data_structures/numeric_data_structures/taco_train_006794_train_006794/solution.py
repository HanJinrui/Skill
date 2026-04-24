import numpy as np

class Solution:

	def streamAvg(self, arr, n):
		return [np.average(arr[:i + 1]) for i in range(len(arr))]
