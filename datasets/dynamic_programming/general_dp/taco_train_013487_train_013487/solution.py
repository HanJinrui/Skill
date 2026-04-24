class Solution:

	def NoOfChicks(self, N):
		(arr, k) = ([1], 1)
		for i in range(1, N):
			if i >= 6:
				k -= arr[i - 6]
			arr.append(k * 2)
			k += arr[i]
		return k
