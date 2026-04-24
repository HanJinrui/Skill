class Solution:

	def modify(self, N):
		ans = '-'
		for x in str(N):
			if x != ans[-1]:
				ans += x
		return int(ans[1:])
