class Solution:

	def find(self, arr, n):
		i = 0
		flag = True
		while flag:
			i += 1
			flag = False
			num = i
			for item in arr:
				num = num * 2 - item
				if num < 0:
					flag = True
					break
		return i
