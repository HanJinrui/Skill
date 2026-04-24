class Solution:

	def checkPangram(self, s):
		import re
		s = re.sub('[^a-zA-Z]', '', s).lower()
		return len(set(s)) == 26
