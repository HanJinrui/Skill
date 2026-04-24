class Solution:

	def getPizza(self, X, S, M, L, CS, CM, CL):
		tab = [0] * 10000
		for i in range(1, X + 1):
			tab[i] = min(CS + tab[i - S], CM + tab[i - M], CL + tab[i - L])
		return tab[X]
