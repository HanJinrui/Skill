import math

def squareSum(N):
	return N * (N + 1) * (2 * N + 1) // 6

def linearSum(N):
	return N * (N + 1) // 2

def getFunctionValue(A, B, C, L, R):
	if R < L:
		return 0
	dxx = squareSum(R) - squareSum(L - 1)
	dx = linearSum(R) - linearSum(L - 1)
	d = R - (L - 1)
	return A * dxx + B * dx + C * d

def phawinRoundDown(v):
	l = int(v)
	r = l + 1
	if r - v < 1e-06:
		return r
	else:
		return l

def phawinRoundUp(v):
	l = int(v)
	r = l + 1
	if v - l < 1e-06:
		return l
	else:
		return r

def solve(L, R):
	ALL = linearSum(R) - linearSum(L - 1)
	N = R - L + 1
	A = 1
	B = -(N + 1)
	C = L + N - 1
	if B * B - 4 * A * C <= 0:
		fv = getFunctionValue(A, B, C, 1, N)
		return ALL - fv
	else:
		sq = math.sqrt(B * B - 4 * A * C)
		k1 = (-B - sq) / 2
		k2 = (-B + sq) / 2
		k1 = min(phawinRoundDown(k1), N)
		k2 = max(phawinRoundUp(k2), 1)
		r1 = getFunctionValue(A, B, C, 1, k1)
		r2 = getFunctionValue(A, B, C, k2, N)
		return ALL - (r1 + r2)

def driver():
	TC = int(input())
	for run_id in range(TC):
		data = input().split()
		L = int(data[0])
		R = int(data[1])
		ans = solve(L, R)
		print(ans)
driver()
