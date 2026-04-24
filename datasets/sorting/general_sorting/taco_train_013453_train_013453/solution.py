class Solution:

	def shouldPunish(self, roll, marks, n, avg):
		count = 0
		for i in range(n):
			for j in range(n - i - 1):
				if roll[i] > roll[j + 1]:
					count += 1
		ans = (sum(marks) - count * 2) / n
		if ans <= avg:
			return 0
		else:
			return 1
