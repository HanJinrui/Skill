class Solution:

	def evaluatePostfix(self, s):
		st = []
		for i in s:
			if i in '0123456789':
				st.append(i)
			else:
				p2 = st.pop()
				p1 = st.pop()
				res = eval(p1 + i + p2)
				st.append(str(int(res)))
		return st[-1]
