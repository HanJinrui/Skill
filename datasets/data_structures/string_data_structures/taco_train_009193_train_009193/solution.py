class Solution:

	def getCount(self, S, N):
		res = S[0]
		for i in S[1:]:
			if i != res[-1]:
				res += i
		count = 0
		for i in set(res):
			if res.count(i) == N:
				count += 1
		return count
