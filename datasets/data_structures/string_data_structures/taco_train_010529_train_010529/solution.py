from itertools import permutations

class Solution:

	def maxPerm(self, N, M):
		ans = [list(i) for i in permutations(str(N))]
		ans = [int(''.join(i)) for i in ans if int(''.join(i)) <= M]
		return max(ans) if len(ans) > 0 else -1
