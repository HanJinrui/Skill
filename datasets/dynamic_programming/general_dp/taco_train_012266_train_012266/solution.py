class Solution:

	def bellNumber(self, n):
		arr = [[1]]
		for i in range(1, n):
			tmp = [arr[i - 1][i - 1]]
			for j in range(1, i + 1):
				tmp.append((arr[i - 1][j - 1] + tmp[j - 1]) % (10 ** 9 + 7))
			arr.append(tmp)
		return arr[-1][-1] % (10 ** 9 + 7)
