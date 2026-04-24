class Solution:

	def groupRows(self, M, n):
		setti = set()
		for item in M:
			if '1' in item:
				setti.add(item)
		return [i for i in range(len(setti))] if setti else [-1]
