class Solution:

	def maxFruits(self, arr, n, m):
		sumo = sum(arr[:m])
		ans = sumo
		for i in range(1, n):
			sumo += arr[(i + m - 1) % n]
			sumo -= arr[i - 1]
			ans = max(ans, sumo)
		return ans
