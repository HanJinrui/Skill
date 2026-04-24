class Solution:

	def areKAnagrams(self, str1, str2, k):
		if len(str1) != len(str2):
			return False
		from collections import Counter
		c1 = Counter(str1)
		c2 = Counter(str2)
		if sum((c2 - c1).values()) <= k:
			return True
		else:
			False
