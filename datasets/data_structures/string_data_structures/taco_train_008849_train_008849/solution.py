class Solution:

	def removeComments(self, code):
		import re
		code = re.sub('/[*].*[*]/', '', code)
		code = re.sub('//.*\\\\n', '', code)
		return code
