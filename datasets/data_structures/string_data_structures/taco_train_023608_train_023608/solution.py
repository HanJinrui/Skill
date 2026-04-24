import re

class Solution:

	def patternCount(self, S):
		return len(re.findall('(?=(10+1))', S))
