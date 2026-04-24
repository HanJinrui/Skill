from bisect import bisect_left

class Solution:

	def removeStudents(self, H, N):
		A = []
		for i in H:
			j = bisect_left(A, i)
			if j == len(A):
				A.append(i)
			else:
				A[j] = i
		return N - len(A)
