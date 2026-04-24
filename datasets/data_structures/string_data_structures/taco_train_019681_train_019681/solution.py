class Solution:

	def stringComparsion(self, s1, s2):
		for i in range(min(len(s1), len(s2))):
			if s1[i] > s2[i]:
				return 1
			elif s1[i] < s2[i]:
				return -1
			if s1[i] == s2[i]:
				if s1[i] == 'n':
					if i + 1 < len(s1) and s1[i + 1] == 'g' and (i + 1 >= len(s2) or s2[i + 1] != 'g'):
						return 1
					elif i + 1 < len(s2) and s2[i + 1] == 'g' and (i + 1 >= len(s1) or s1[i + 1] != 'g'):
						return -1
		if len(s1) > len(s2):
			return 1
		elif len(s2) > len(s1):
			return -1
		return 0
