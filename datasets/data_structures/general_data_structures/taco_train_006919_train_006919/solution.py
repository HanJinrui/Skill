class Solution:

	def findMaxOddSubarraySum(self, arr, n):
		s = 0
		od = 999999999
		f = 0
		for i in arr:
			if i > 0:
				s += i
			if i % 2 != 0:
				f = 1
				if abs(i) < od:
					od = abs(i)
		if f == 0:
			return -1
		if s % 2 == 0:
			return s - od
		return s
