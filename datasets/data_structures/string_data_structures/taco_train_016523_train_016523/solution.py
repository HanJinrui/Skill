class Solution:

	def removeChars(ob, s, s2):
		j = ''
		for i in s:
			if i not in s2:
				j += i
		return j
