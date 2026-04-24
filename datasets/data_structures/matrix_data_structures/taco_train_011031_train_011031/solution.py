class Solution:

	def FindPath(self, str):
		curr = 0
		total = 0
		for i in str:
			temp = ord(i) - 97
			x = abs(temp % 5 - curr % 5)
			y = abs(temp // 5 - curr // 5)
			curr = temp
			total += x + y + 1
		return total
