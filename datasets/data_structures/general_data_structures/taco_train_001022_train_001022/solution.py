class Solution:

	def recreationalSpot(self, arr, n):
		st = []
		m = -1000000000.0
		for i in arr[::-1]:
			if i < m:
				return True
			while st and st[-1] < i:
				m = st.pop()
			st.append(i)
		return False
