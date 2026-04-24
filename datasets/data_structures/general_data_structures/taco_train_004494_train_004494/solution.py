class Solution:

	def checkUnimodal(self, arr, n):
		second = False
		for i in range(n - 1):
			if second == False and arr[i] <= arr[i + 1]:
				continue
			if arr[i] > arr[i + 1]:
				second = True
				continue
			return False
		return True
