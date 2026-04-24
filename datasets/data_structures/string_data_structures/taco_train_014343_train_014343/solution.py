import re

class Solution:

	def findSum(self, s):
		return sum(map(int, re.findall('\\d+', s)))
