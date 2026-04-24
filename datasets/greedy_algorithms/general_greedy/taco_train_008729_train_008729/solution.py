class Solution:

	def isPossible(self, S, N, X, A):
		l = [S]
		sum_ = S
		for a in A:
			t = sum_
			sum_ += a
			l.append(sum_)
			sum_ += t
		for i in range(len(l) - 1, -1, -1):
			if l[i] <= X:
				X -= l[i]
		return X == 0
