class Solution:

	def increment(self, arr, N):
		if arr[-1] < 9:
			arr[-1] += 1
			return arr
		s = ''.join(map(str, arr))
		return list(str(int(s) + 1))
