from collections import Counter

class Solution:

	def mostFrequentWord(self, arr, n):
		dic = Counter(arr)
		ans = ''
		freq = 0
		for i in arr:
			if dic[i] >= freq:
				freq = dic[i]
				ans = i
				dic[i] -= 1
		return ans
