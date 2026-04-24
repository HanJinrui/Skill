def LongestPalindromeSubString(text):
	if len(text) == 1:
		return text
	s = '#'.join('^{}$'.format(text))
	n = len(s)
	L = [0] * n
	(C, R) = (0, 0)
	mLen = 0
	mLenPos = 0
	for i in range(1, n - 1):
		L[i] = R > i and min(L[2 * C - i], R - i)
		while s[i + L[i] + 1] == s[i - L[i] - 1]:
			L[i] += 1
		if L[i] > mLen:
			mLen = L[i]
			mLenPos = i
		if i + L[i] > R:
			C = i
			R = i + L[i]
	start = (mLenPos - mLen) // 2
	end = start + mLen
	return text[start:end]
