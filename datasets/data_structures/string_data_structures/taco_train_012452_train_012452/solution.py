class Solution:

	def decodeIt(self, Str, k):
		t = ''
		for i in Str:
			if i.isdigit():
				t = t * int(i)
			else:
				t += i
		return t[k - 1]
