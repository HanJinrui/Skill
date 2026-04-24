import numpy as np
import math

class Solution:

	def buzzTime(self, N, M, L, H, A):
		H = np.array(H)
		A = np.array(A)
		n = math.ceil(min((L - H) / A))
		H = H + n * A
		while True:
			sum_res = np.sum(H[H > L])
			if sum_res >= M:
				return n
			H = H + A
			n += 1
