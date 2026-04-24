class Solution:

	def TopK(self, array, k):
		d = dict()
		for i in array:
			d[i] = d[i] + 1 if d.get(i) else 1
		res = sorted(d, key=lambda k: (d[k], k), reverse=True)
		return res[:k]
