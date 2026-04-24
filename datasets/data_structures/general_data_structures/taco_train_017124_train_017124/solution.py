class Solution:

	def getDigitDiff1AndLessK(self, arr, n, k):
		ans = []
		for i in arr:
			if i < k and len(str(i)) > 1:
				temp = str(i)
				if all((abs(int(temp[j]) - int(temp[j - 1])) == 1 for j in range(1, len(temp)))):
					ans.append(i)
		return ans
