import re

class Solution:

	def isPatternPresent(self, S, P):
		return int(bool(re.search(P, S)))
