class Solution:

	def convertToWords(self, n):
		A = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ', 'ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']
		B = ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety ']

		def helper(n, s):
			str = ''
			if n > 19:
				str += B[n // 10] + A[n % 10]
			else:
				str += A[n]
			if n:
				str += s
			return str
		s = ''
		s += helper(n // 10 ** 7, 'crore ')
		s += helper(n // 10 ** 5 % 100, 'lakh ')
		s += helper(n // 10 ** 3 % 100, 'thousand ')
		s += helper(n // 10 ** 2 % 10, 'hundred ')
		if n > 100 and n % 100:
			s += 'and '
		s += helper(n % 100, '')
		return s
