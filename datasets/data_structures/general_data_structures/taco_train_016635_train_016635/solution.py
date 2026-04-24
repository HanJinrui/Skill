class Solution:

	def countPair(self, h1, h2, n1, n2, x):
		setti = set()
		while h1:
			setti.add(h1.data)
			h1 = h1.next
		count = 0
		while h2:
			count += x - h2.data in setti
			h2 = h2.next
		return count
