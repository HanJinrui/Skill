T = int(input())
for i in range(T):
	A = list(map(int, input().split()))
	if sum(A[::2]) > sum(A[1::2]):
		print(1)
	elif sum(A[::2]) == sum(A[1::2]):
		print(0)
	else:
		print(2)
