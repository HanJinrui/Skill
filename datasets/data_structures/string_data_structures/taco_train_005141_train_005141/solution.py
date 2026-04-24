class Solution:

	def amendSentence(self, s):
		t = ''
		for i in s:
			if i.isupper():
				t += ' ' + i.lower()
			else:
				t += i
		return t.lstrip()
