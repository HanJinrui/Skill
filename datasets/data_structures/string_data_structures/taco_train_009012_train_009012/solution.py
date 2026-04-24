import re

class Solution:

	def match(self, pattern, string):
		regex = re.compile('^' + pattern.replace('*', '.*').replace('?', '.') + '$')
		return regex.match(string) is not None
