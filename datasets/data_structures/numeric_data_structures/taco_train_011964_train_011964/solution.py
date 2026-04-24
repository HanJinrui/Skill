def maxArea(A, le):
	r = le - 1
	l = 0
	a = 0
	while l < r:
		a = max(a, min(A[l], A[r]) * (r - l))
		if A[l] < A[r]:
			l += 1
		else:
			r -= 1
	return a
