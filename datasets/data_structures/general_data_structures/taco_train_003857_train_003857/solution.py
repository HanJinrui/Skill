class Solution:

	def modifyAndRearrangeArr(self, arr, n):
		j = 1
		while j < n:
			if arr[j] == arr[j - 1]:
				arr[j - 1] *= 2
				arr[j] = 0
			j += 1
		a = []
		z = []
		for i in arr:
			if i == 0:
				z.append(0)
			else:
				a.append(i)
		arr[:] = a + z
		return arr
