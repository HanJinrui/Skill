class Solution:

	def isProduct(self, arr, n, x):
		st = set()
		for i in arr:
			if i != 0 and x / i in st:
				return True
			else:
				st.add(i)
