class Solution:

	def areAnagram(ob, s1, s2):
		if sorted(s1) == sorted(s2):
			return 1
		return 0
