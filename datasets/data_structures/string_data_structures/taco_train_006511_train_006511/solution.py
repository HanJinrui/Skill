class Solution:

	def winner(self, arr, n):
		l = []
		arr = sorted(arr)
		l = [arr.count(arr[i]) for i in range(n)]
		return (arr[l.index(max(l))], max(l))
