class Solution:

	def fillingBucket(self, N):
		(one, two) = (1, 1)
		for i in range(N - 1):
			(one, two) = ((one + two) % 10 ** 8, one)
		return one
