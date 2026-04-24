N = int(input())
K = int(input())
C = [int(input()) for n in range(0, N)]
C.sort()
(i, s, u) = (0, 0, 0)
while i < K:
	u += i * C[i] - s
	s += C[i]
	i += 1
umin = u
while i < N:
	u += (K - 1) * (C[i] + C[i - K]) - 2 * (s - C[i - K])
	s += C[i] - C[i - K]
	i += 1
	if u < umin:
		umin = u
print(umin)
