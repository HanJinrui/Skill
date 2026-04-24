def init(A, n):
	retA = [0] * (n + 1)
	B = [0] * (n + 1)
	tmp = 0
	for i in range(n):
		tmp ^= A[i]
		B[i + 1] = tmp
		retA[i + 1] += retA[i] + tmp
	return (retA, B)
(n, q) = list(map(int, input().rstrip().split()))
A = list(map(int, input().rstrip().split()))
(newA, B) = init(A, n)
while q > 0:
	(x, y, k) = list(map(int, input().rstrip().split()))
	num = newA[y + 1] - newA[x]
	if B[x]:
		num = y + 1 - x - num
	size = y - x + 2
	num = abs(int(size / 2)) if k else num
	print(num * (size - num))
	q -= 1
