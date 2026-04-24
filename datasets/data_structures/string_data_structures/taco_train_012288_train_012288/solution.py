class Solution:

	def allPossibleSubsequences(ob, s):
		res = set()

		def fun(ind, st):
			if ind >= len(s):
				if len(st) >= 2 and st[0] in ['a', 'e', 'i', 'o', 'u'] and (st[-1] not in ['a', 'e', 'i', 'o', 'u']):
					res.add(st)
				return
			fun(ind + 1, st + s[ind])
			fun(ind + 1, st)
		fun(0, '')
		return sorted(list(res))
