import sys
from itertools import accumulate
input = sys.stdin.readline
n = int(input())
P = tuple(map(int, input().split()))
A = tuple(map(int, input().split()))
seg_el = 1 << (n + 1).bit_length()
SEGMIN = [0] * (2 * seg_el)
SEGADD = [0] * (2 * seg_el)
for i in range(n):
	SEGMIN[P[i] + seg_el] = A[i]
SEGMIN = list(accumulate(SEGMIN))
for i in range(seg_el - 1, 0, -1):
	SEGMIN[i] = min(SEGMIN[i * 2], SEGMIN[i * 2 + 1])

def adds(l, r, x):
	L = l + seg_el
	R = r + seg_el
	while L < R:
		if L & 1:
			SEGADD[L] += x
			L += 1
		if R & 1:
			R -= 1
			SEGADD[R] += x
		L >>= 1
		R >>= 1
	L = l + seg_el >> 1
	R = r + seg_el - 1 >> 1
	while L != R:
		if L > R:
			SEGMIN[L] = min(SEGMIN[L * 2] + SEGADD[L * 2], SEGMIN[1 + L * 2] + SEGADD[1 + L * 2])
			L >>= 1
		else:
			SEGMIN[R] = min(SEGMIN[R * 2] + SEGADD[R * 2], SEGMIN[1 + R * 2] + SEGADD[1 + R * 2])
			R >>= 1
	while L != 0:
		SEGMIN[L] = min(SEGMIN[L * 2] + SEGADD[L * 2], SEGMIN[1 + L * 2] + SEGADD[1 + L * 2])
		L >>= 1
S = tuple(accumulate(A))
ANS = 1 << 31
for i in range(n - 1):
	adds(P[i], n + 1, -A[i] * 2)
	ANS = min(ANS, SEGMIN[1] + S[i])
print(ANS)
