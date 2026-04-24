class Solution:

	def findLongestWord(ob, S, d):
		for i in sorted(d, key=lambda x: (-len(x), x)):
			it = iter(S)
			if all((x in it for x in i)):
				return i
		return ''
