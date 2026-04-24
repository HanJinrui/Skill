class Solution:

	def nearestSmallestTower(self, arr):
		n = len(arr)
		ans = [-1] * n
		s1 = []
		for i in range(n):
			while s1 and arr[s1[-1]] >= arr[i]:
				s1.pop()
			if s1:
				ans[i] = s1[-1]
			s1.append(i)
		s1.clear()
		for i in range(n - 1, -1, -1):
			while s1 and arr[s1[-1]] >= arr[i]:
				s1.pop()
			if s1:
				if ans[i] == -1:
					ans[i] = s1[-1]
				elif i - ans[i] > s1[-1] - i:
					ans[i] = s1[-1]
				elif i - ans[i] == s1[-1] - i:
					if arr[ans[i]] > arr[s1[-1]]:
						ans[i] = s1[-1]
			s1.append(i)
		return ans
