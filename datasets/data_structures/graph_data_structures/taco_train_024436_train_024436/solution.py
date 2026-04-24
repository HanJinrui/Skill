class Solution:

	def getPar(self, a, par):
		if a != par[a]:
			par[a] = self.getPar(par[a], par)
		return par[a]

	def union_(self, a, b, par, rank1):
		x = self.getPar(a, par)
		y = self.getPar(b, par)
		par[x] = y

	def isConnected(self, x, y, par, rank1):
		return self.getPar(x, par) == self.getPar(y, par)
