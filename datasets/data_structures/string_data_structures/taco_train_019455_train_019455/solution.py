class Solution:

	def areElementsContiguous(self, arr, n):
		hm = {}
		for i in arr:
			if i in hm:
				del hm[i]
			elif i == 'END':
				hm.clear()
			else:
				hm[i] = 1
		return len(hm)
