T = int(input())
for _ in range(T):
	n = int(input())
	A = list(map(int, input().split()))
	A.sort()
	c = 0
	for i in range(n):
		if A[i] > i + 1:
			c = -1
			break
		c += i + 1 - A[i]
	print(c)
