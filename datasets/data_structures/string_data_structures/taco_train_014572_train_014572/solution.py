class Solution:

	def calcDiff(self, S):
		ls = []
		ls = S.split()
		h = 0
		e = 0
		vw = 'aeiouAEIOU'
		for word in ls:
			vol = 0
			conc = 0
			for ch in word:
				if ch in vw:
					vol += 1
				else:
					conc += 1
			if conc > vol:
				h += 1
			else:
				e += 1
		return 5 * h + 3 * e
