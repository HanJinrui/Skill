class Solution:

	def getCount(self, N):
		d = [[0, 8], [1, 2, 4], [2, 3, 5, 1], [3, 2, 6], [4, 1, 5, 7], [5, 6, 4, 2, 8], [6, 3, 5, 9], [7, 4, 8], [8, 7, 9, 5, 0], [9, 8, 6]]
		l = [1] * 10
		l_new = [0] * 10
		for dig in range(1, N):
			for i in range(10):
				temp_sum = [l[x] for x in d[i]]
				l_new[i] = sum(temp_sum)
			l = l_new.copy()
		return sum(l)
