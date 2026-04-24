class Solution:

	def pyramidForm(self, arr, n):
		left = [0] * n
		right = [0] * n
		arr = list(arr)
		left[0] = 1
		for i in range(1, n):
			left[i] = min(arr[i], left[i - 1] + 1)
		right[-1] = 1
		for i in range(n - 2, -1, -1):
			right[i] = min(arr[i], right[i + 1] + 1)
		mini = float('inf')
		summe = sum(arr)
		for i in range(n):
			curr = summe - min(left[i], right[i]) ** 2
			mini = min(mini, curr)
		return mini
