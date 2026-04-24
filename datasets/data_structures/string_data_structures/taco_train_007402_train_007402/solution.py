class Solution:

	def unique_substring_sum(self, s, k):
		if len(s) % k != 0:
			return -1
		a = []
		for i in range(0, len(s), k):
			a.append(int(s[i:i + k], 2))
		k = sum(set(a))
		return k
