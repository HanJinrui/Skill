class Solution:

	def prefixSuffixString(self, s1, s2) -> int:
		y = set(s1)
		for x in s1:
			for i in range(1, len(x)):
				y.add(x[:i])
				y.add(x[-i:])
		return sum((x in y for x in s2))
