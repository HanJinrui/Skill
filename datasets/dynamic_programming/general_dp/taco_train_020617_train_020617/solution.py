class Solution:

	def maxSumSequence(self, N, A):
		lis = [[i] for i in A]
		for i in range(1, len(A)):
			for j in range(0, i):
				if A[i] > A[j] and sum(lis[i]) < sum(lis[j]) + A[i]:
					lis[i] = lis[j].copy()
					lis[i].append(A[i])
		ans = [0]
		for i in lis:
			if sum(i) > sum(ans):
				ans = i.copy()
		return ans
