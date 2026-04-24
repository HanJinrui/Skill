class Solution:

	def leftRight(self, arr, n):
		vis = [0] * n
		for i in arr:
			try:
				if vis[i] == 1:
					vis[n - i - 1] = 1
				else:
					vis[i] = 1
			except:
				return False
		if 0 in vis:
			return False
		return True
