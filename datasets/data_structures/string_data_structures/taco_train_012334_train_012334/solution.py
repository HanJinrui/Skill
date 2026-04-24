class Solution:

	def stringFilter(self, str):
		import re
		return re.sub('b|ac', '', str)
