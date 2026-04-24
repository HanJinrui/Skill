class Solution:

	def rotateMatrix(self, N, M, K, Mat):
		K = K % M
		return [row[K:] + row[:K] for row in Mat]
