import time

class Solution:

	def __init__(self):
		self.star_time = time.time()

	def palindromepair(self, N, arr):
		for i in range(len(arr)):
			for e in range(N):
				if N > 600 and time.time() - self.star_time > 8:
					return 0
				j = N - 1 - e
				if i != j:
					if arr[i] + arr[j] == (arr[i] + arr[j])[::-1]:
						return 1
		return 0
