class Solution:

	def maxValueOfExpression(self, a, n):
		case1 = [0] * n
		case2 = [0] * n
		for i in range(n):
			case1[i] = int(a[i]) + i
			case2[i] = int(a[i]) - i
		res1 = abs(max(case1) - min(case1))
		res2 = abs(max(case2) - min(case2))
		return max(res1, res2)
