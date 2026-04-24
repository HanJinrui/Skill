class Solution:

	def maximumProfit(self, N, C, w, p):
		ratios = sorted([[P / W, W, P] for (W, P) in zip(w, p) if W ** (1 / 2) != int(W ** (1 / 2))], reverse=True)
		sm = 0
		for (R, W, P) in ratios:
			if C > W:
				sm += P
				C -= W
			else:
				sm += round(C * R, 3)
				break
		return sm
