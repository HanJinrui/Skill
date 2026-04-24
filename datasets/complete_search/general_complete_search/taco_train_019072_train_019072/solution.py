class Solution:

	def AllParenthesis(self, n):
		res = []

		def recur(st, op, cl):
			if op == cl == n:
				res.append(st[:])
				return
			if op < n:
				recur(st + '(', op + 1, cl)
			if cl < op:
				recur(st + ')', op, cl + 1)
		recur('', 0, 0)
		return res
