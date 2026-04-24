class Solution:

	def ExcelColumn(self, N):
		s = ''
		while N:
			x = 65 + (N - 1) % 26
			s = chr(x) + s
			N = (N - 1) // 26
		return s
