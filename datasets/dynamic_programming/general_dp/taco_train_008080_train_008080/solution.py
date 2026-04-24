class Solution:

	def inverse(self, s, rem):
		return pow(s, rem - 2, rem)

	def getSum(self, X, Y, Z):
		rem = 10 ** 9 + 7
		(fact, ons) = ([1], [0])
		for i in range(1, X + Y + Z + 1):
			fact.append(fact[-1] * i % rem)
			ons.append((ons[-1] * 10 + 1) % rem)
		output = 0
		for i in range(X + 1):
			for j in range(Y + 1):
				for k in range(Z + 1):
					s = i + j + k
					total = 4 * i + 5 * j + 6 * k
					output = (output + total * fact[s - 1] * ons[s] * self.inverse(fact[i] * fact[j] * fact[k], rem)) % rem
		return output
