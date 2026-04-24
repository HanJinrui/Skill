import math
Q = int(input())
for qi in range(Q):
	K = int(input())
	A = int(input(), 16)
	B = int(input(), 16)
	C = int(input(), 16)
	n = int(math.log(max([A, B, C]), 2)) + 1
	m = pow(2, n)
	notA = m - A - 1
	notB = m - B - 1
	notC = m - C - 1
	newA = A & C
	K -= bin(A - newA).count('1')
	A = newA
	newB = B & C
	K -= bin(B - newB).count('1')
	B = newB
	newB = B | C - A
	K -= bin(newB - B).count('1')
	B = newB
	if K < 0:
		print(-1)
		continue
	mask = m
	while K > 0 and mask > 1:
		mask >>= 1
		if mask & A & B:
			A ^= mask
			K -= 1
		elif mask & A and K > 1:
			A ^= mask
			B |= mask
			K -= 2
	print(hex(A)[2:].upper())
	print(hex(B)[2:].upper())
