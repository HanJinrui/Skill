class Solution:

	def minStep(self, H, U, D):
		return int((H - D) / (U - D) + 1)
