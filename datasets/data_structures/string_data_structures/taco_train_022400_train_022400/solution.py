from itertools import permutations

class Solution:

	def isDivisible8(self, S):
		if len(S) >= 3:
			p = list(set(permutations(S, 3)))
		else:
			p = list(set(permutations(S)))
		p = [int(''.join(i)) for i in p]
		for num in p:
			if num % 8 == 0:
				return True
		return False
