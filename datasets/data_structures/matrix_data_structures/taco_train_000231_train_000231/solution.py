class Solution:

	def largestSubsquare(self, N, A):
		left_c = [[0] * N for i in range(N)]
		top_c = [[0] * N for i in range(N)]
		for i in range(N):
			for j in range(N):
				if A[i][j] == 'X':
					left_c[i][j] = (left_c[i][j - 1] if j > 0 else 0) + 1
					top_c[i][j] = (top_c[i - 1][j] if i > 0 else 0) + 1
		max_len = 0
		for i in range(N - 1, -1, -1):
			for j in range(N - 1, -1, -1):
				val = min(left_c[i][j], top_c[i][j])
				while val > max_len:
					if top_c[i][j - val + 1] >= val and left_c[i - val + 1][j] >= val:
						max_len = max(max_len, val)
					val -= 1
		return max_len
