class Solution:

	def count(self, s):
		a = [0, 0, 0, 0]
		for i in s:
			if i.isupper():
				a[0] += 1
			elif i.islower():
				a[1] += 1
			elif i.isdigit():
				a[2] += 1
			else:
				a[3] += 1
		return a
