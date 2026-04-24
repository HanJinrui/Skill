class Solution:

	def removeKdigits(self, S, K):
		s = []
		for i in S:
			while K > 0 and s and (s[-1] > i):
				K -= 1
				s.pop()
			s.append(i)
		s = s[:len(s) - K]
		res = ''.join(s)
		return str(int(res)) if res else '0'
