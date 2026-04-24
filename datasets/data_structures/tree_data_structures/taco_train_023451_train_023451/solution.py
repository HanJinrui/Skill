class Solution:

	def supplyVaccine(self, root):
		ans = [0]

		def rec(nod):
			if nod is None:
				return 2
			lef = rec(nod.left)
			righ = rec(nod.right)
			if lef == 0 or righ == 0:
				ans[0] += 1
				return 1
			elif lef == 2 and righ == 2:
				return 0
			return 2
		if rec(root) == 0:
			ans[0] += 1
		return ans[0]
