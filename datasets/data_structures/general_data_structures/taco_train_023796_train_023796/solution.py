import heapq

class Solution:

	def printKClosest(self, arr, n, k, x):
		return heapq.nsmallest(k, arr, key=lambda i: (abs(x - i) if x != i else i + float('inf'), -1 * i))
