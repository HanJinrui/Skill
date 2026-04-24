class Solution:

	def isStringExist(self, arr, n, s):
		l = len(s)
		for i in arr:
			count = 0
			if len(i) == l:
				for j in range(len(i)):
					if i[j] != s[j]:
						count += 1
			if count == 1:
				return True
		return False
