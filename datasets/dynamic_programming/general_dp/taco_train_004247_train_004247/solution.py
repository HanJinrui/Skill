from bisect import *

class Solution:

	def maxSumLis(self, Arr, n):
		temp = []
		sum = 0
		S = [0] * (n + 1)
		for i in range(n):
			sum += Arr[i]
			pos = bisect_left(temp, Arr[i])
			if pos == len(temp):
				temp.append(Arr[i])
			else:
				temp[pos] = Arr[i]
			S[pos + 1] = S[pos] + Arr[i]
		return sum - S[len(temp)]
