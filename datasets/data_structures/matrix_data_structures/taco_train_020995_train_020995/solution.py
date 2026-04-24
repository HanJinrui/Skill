import numpy as np

class Solution:

	def sortedMatrix(self, N, Mat):
		Mat = np.array(Mat)
		Mat = Mat.flatten()
		Mat = np.sort(Mat)
		Mat = Mat.reshape(N, N)
		return Mat
