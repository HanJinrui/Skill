class Solution:

	def FindQuery(self, nums, Query):
		n = len(nums)
		s2 = [0]
		s1 = [0]
		s0 = [0]
		m = 1000000007
		ans = []
		for i in range(1, n + 1):
			s2.append((s2[i - 1] + i * i * nums[i - 1]) % m)
			s1.append((s1[i - 1] + i * nums[i - 1]) % m)
			s0.append((s0[i - 1] + nums[i - 1]) % m)
		q = len(Query)
		for i in range(q):
			l = Query[i][0]
			r = Query[i][1]
			ss = s2[r] - s2[l - 1]
			ls = s1[r] - s1[l - 1]
			zs = s0[r] - s0[l - 1]
			d = l - 1
			ans.append((ss - 2 * d * ls + d * d * zs) % m)
		return ans
