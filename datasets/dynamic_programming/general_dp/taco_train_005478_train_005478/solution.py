from bisect import bisect_left

class Solution:

	def longestSubsequence(self, arr, n):
		seq = []
		for a in arr:
			i = bisect_left(seq, a)
			if i == len(seq):
				seq.append(a)
			else:
				seq[i] = a
		return len(seq)
