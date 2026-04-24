class Solution:

	def Reduced_String(self, k, s):
		can = True
		while can:
			can = False
			cset = set(s)
			for ch in cset:
				if ch * k in s:
					s = s.replace(ch * k, '')
					can = True
		return s
