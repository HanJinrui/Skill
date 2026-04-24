class Solution:

	def maxValue(self, arr, N):
		a = []
		b = []
		for i in range(N):
			a.append(arr[i] - i)
			b.append(arr[i] + i)
		ans1 = max(a) - min(a)
		ans2 = max(b) - min(b)
		return max(ans1, ans2)
