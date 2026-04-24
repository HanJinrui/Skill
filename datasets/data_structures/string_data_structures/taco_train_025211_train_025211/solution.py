class Solution:

	def longestCommonPrefix(self, arr, n):
		arr.sort()
		s = arr[0]
		sum = ''
		for i in range(len(s)):
			if s[i] == arr[n - 1][i]:
				sum += s[i]
			else:
				break
		return sum if len(sum) > 0 else -1
