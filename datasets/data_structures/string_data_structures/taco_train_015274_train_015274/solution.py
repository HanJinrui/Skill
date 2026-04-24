import re

class Solution:

	def extractMaximum(self, S):
		ans = [int(i) for i in re.findall('\\d+', S)]
		return max(ans) if len(ans) > 0 else -1
