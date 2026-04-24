class Solution:

	def subsets(self, A):
		ans = [[]]
		for i in A:
			ans += [j + [i] for j in ans]
		return sorted(ans)
