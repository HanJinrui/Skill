class Solution:

	def totalFine(self, n, date, car, fine):
		total_fine = 0
		for i in range(n):
			if car[i] % 2 != date % 2:
				total_fine += fine[i]
		return total_fine
