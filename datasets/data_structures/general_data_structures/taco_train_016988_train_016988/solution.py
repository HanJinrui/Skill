class Solution:

	def removeDuplicate(self, A, N):
		h = set()
		r = [i for i in A if not (i in h or h.add(i))]
		return r
