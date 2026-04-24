class Solution:

	def removePair(self, s):
		arr = []
		for i in s:
			if arr and arr[-1] == i:
				arr.pop()
			else:
				arr.append(i)
		return ''.join(arr) if arr else '-1'
