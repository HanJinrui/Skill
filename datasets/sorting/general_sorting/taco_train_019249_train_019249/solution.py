class Solution:

	def isPossible(self, per, vac, n):
		vac.sort()
		per.sort()
		for i in range(n):
			if vac[i] < per[i]:
				return 0
		return 1
