class Solution:

	def addPolynomial(self, poly1, poly2):
		mp = {}
		cur = poly1
		while cur:
			try:
				mp[cur.power] += cur.coef
			except KeyError:
				mp[cur.power] = cur.coef
			cur = cur.next
		cur = poly2
		while cur:
			try:
				mp[cur.power] += cur.coef
			except KeyError:
				mp[cur.power] = cur.coef
			cur = cur.next
		res = Linked_List()
		lst = list(mp.items())
		for i in lst[::-1]:
			res.insert(i[1], i[0])
		return res.head
