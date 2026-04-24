class Solution:

	def maximizeArray(self, arr1, arr2, n):
		arr3 = arr2 + arr1
		a = arr3
		arr3 = list(set(arr3))
		arr3 = sorted(arr3)
		r = []
		res = list(reversed(arr3))
		check = set()
		res = set(res[0:n])
		for i in a:
			if i in res and i not in check:
				check.add(i)
				r.append(i)
		return r
