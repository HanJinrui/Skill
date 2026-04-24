class Solution:

	def findMaxSum(self, N, M, Mat):
		maxi = -1
		for i in range(N - 2):
			for j in range(M - 2):
				summa = 0
				summa += sum(Mat[i][j:j + 3])
				summa += Mat[i + 1][j + 1]
				summa += sum(Mat[i + 2][j:j + 3])
				maxi = max(maxi, summa)
		return maxi
