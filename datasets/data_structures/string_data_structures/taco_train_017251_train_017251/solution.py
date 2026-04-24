class Solution:

	def all_palindromes(self, s):
		res = []

		def palin(ssf, l):
			nonlocal odd
			if len(ssf) == l:
				if odd:
					res.append(ssf + odd + ssf[::-1])
				else:
					res.append(ssf + ssf[::-1])
				return
			for i in h.keys():
				if h[i] > 0:
					h[i] -= 1
					palin(ssf + i, l)
					h[i] += 1
		h = {}
		l = 0
		odd = None
		for i in s:
			h[i] = h.get(i, 0) + 1
		for i in h.keys():
			if odd and h[i] % 2:
				return []
			if not odd and h[i] % 2:
				odd = i
			h[i] = h[i] // 2
			l += h[i]
		palin('', l)
		res.sort()
		return res
