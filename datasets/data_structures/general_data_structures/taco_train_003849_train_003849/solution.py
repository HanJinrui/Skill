class Solution:

	def minOperations(self, arr, n, k):
		count = 0
		import heapq
		heapq.heapify(arr)
		while arr[0] < k:
			try:
				heapq.heappush(arr, heapq.heappop(arr) + heapq.heappop(arr))
			except IndexError:
				return -1
			count += 1
		return count
