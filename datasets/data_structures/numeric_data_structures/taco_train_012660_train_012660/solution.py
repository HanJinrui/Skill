class Solution:

	def unvisitedLeaves(self, N, leaves, frogs):
		ju = set(frogs)
		ans = set()
		for j in ju:
			for i in range(j, leaves + 1, j):
				ans.add(i)
		return leaves - len(ans)
