class Solution:

	def Anagrams(self, words, n):
		res = {}
		for i in words:
			s = str(sorted(i))
			if s in res:
				res[s].append(i)
			else:
				res[s] = [i]
		return list(res.values())
