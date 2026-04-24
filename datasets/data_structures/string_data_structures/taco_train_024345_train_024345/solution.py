class Solution:

	def convert(self, s):
		output = ''
		for item in s:
			if item.islower():
				output += chr(219 - ord(item))
			else:
				output += chr(155 - ord(item))
		return output
