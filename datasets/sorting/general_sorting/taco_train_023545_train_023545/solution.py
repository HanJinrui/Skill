class Solution:

	def acceptedProposals(self, arr, n):
		a = sorted(arr)
		return (a[-2], a[1])
