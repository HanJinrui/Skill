def sumDiff(S, n):
	sumF = 0
	sumL = 0
	for i in range(n):
		sumF += S[i] * 2 ** (n - i - 1)
		sumL += S[i] * 2 ** i
	return sumL - sumF
