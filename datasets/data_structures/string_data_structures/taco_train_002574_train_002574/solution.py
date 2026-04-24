class Solution:

	def threeSumClosest(self, arr, target):
		arr.sort()
		c = -9999999
		n = len(arr)
		for i in range(n - 2):
			j = i + 1
			k = n - 1
			while j < k:
				s = arr[i] + arr[j] + arr[k]
				if abs(target - s) < abs(target - c):
					c = s
				elif abs(target - s) == abs(target - c):
					c = max(c, s)
				if s > target:
					k -= 1
				else:
					j += 1
		return c
