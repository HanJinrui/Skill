class Solution:

	def rotateMatrix(self, M, N, Mat):
		l = 0
		r = N - 1
		t = 0
		b = M - 1
		while l < r and t < b:
			p = Mat[t + 1][l]
			for i in range(l, r + 1):
				(Mat[t][i], p) = (p, Mat[t][i])
			t += 1
			for i in range(t, b + 1):
				(Mat[i][r], p) = (p, Mat[i][r])
			r -= 1
			for i in range(r, l - 1, -1):
				(Mat[b][i], p) = (p, Mat[b][i])
			b -= 1
			for i in range(b, t - 1, -1):
				(Mat[i][l], p) = (p, Mat[i][l])
			l += 1
