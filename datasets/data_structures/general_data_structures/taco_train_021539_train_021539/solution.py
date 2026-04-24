class Solution:

	def findGreatest(self, arr, n):
		arr.sort(reverse=True)
		for i in range(n):
			temp = arr[i]
			low = i + 1
			high = n - 1
			while low < high:
				prod = arr[low] * arr[high]
				if prod == temp:
					return prod
				elif prod > temp:
					low += 1
				else:
					high -= 1
		return -1
