class Solution:

	def sevenSegments(self, S, N):
		h = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]
		tl = 0
		for i in range(N):
			tl += h[int(S[i])]
		ans = ''
		for i in range(N):
			for j in range(10):
				cn = tl - h[j]
				if cn >= 2 * (N - 1 - i) and cn <= 7 * (N - i - 1):
					ans += str(j)
					tl = cn
					break
		return ans
