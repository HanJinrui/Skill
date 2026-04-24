def multiply(mat1, mat2, m):
	ans = [[0 for i in range(3)] for j in range(3)]
	for i in range(3):
		for j in range(3):
			for k in range(3):
				ans[i][j] += mat1[i][k] * mat2[k][j] % m
	return ans

def func(mat, n, m):
	if n == 1:
		return mat
	temp = func(mat, n // 2, m)
	if n % 2 == 0:
		return multiply(temp, temp, m)
	return multiply(multiply(temp, temp, m), mat, m)

class Solution:

	def genFibNum(self, a, b, c, n, m):
		mat = [[a, b, 1], [1, 0, 0], [0, 0, 1]]
		if n == 1 or n == 2:
			return 1 % m
		res = func(mat, n - 2, m)
		return (res[0][0] + res[0][1] + c * res[0][2]) % m
