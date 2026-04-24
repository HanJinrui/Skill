class Solution:

	def findMissing(self, arr, n):
		arr.sort()
		ans = ''
		x = 0
		for i in arr:
			if i - x >= 1:
				if i - x == 1:
					ans += str(x) + ' '
				else:
					ans += str(x) + '-' + str(i - 1) + ' '
			x = i + 1
		if not ans:
			return -1
		return ans
