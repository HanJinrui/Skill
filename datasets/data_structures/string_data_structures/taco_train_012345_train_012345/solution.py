class Solution:

	def countCamelCase(self, s):
		return len([x for x in s if x.isupper()])
