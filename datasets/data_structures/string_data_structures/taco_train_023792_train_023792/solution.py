class Solution:

	def findMaxLen(ob, S):
		l = [-1]
		l1 = 0
		for (i, p) in enumerate(S):
			if p == '(':
				l.append(i)
			else:
				l.pop()
				if not l:
					l.append(i)
				else:
					l1 = max(l1, i - l[-1])
		return l1
