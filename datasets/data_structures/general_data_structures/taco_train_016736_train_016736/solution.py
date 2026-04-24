class Solution:

	def InfixtoPostfix(self, exp):
		prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
		post = ''
		st = []
		for i in exp:
			if i == '(':
				st.append(i)
			elif i == ')':
				while st[-1] != '(':
					post += st.pop()
				st.pop()
			elif i not in prec:
				post += i
			else:
				while st and st[-1] != '(' and (prec[i] <= prec[st[-1]]):
					post += st.pop()
				st.append(i)
		while st:
			post += st.pop()
		return post
