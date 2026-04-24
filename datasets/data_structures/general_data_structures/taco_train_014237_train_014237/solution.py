class Solution:

	def minLength(self, s, n):
		lisof = ['21', '12', '34', '43', '56', '65', '78', '87', '09', '90']
		st = []
		for i in s:
			if st and i + st[-1] in lisof:
				st.pop()
			else:
				st.append(i)
		return len(st)
